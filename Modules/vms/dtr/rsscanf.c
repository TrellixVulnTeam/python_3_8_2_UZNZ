/*
 * rsscanf.c
 *
 * vsscanf(), from which the rest of the scanf()
 * family is built
 *
 * Adapted from https://github.com/apache/mynewt-core/blob/master/libc/baselibc/src/vsscanf.c
 *
 */

#include <ctype.h>
#include <stdarg.h>
#include <stddef.h>
#include <inttypes.h>
#include <string.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

#ifndef LONG_BIT
#define LONG_BIT (CHAR_BIT*sizeof(long))
#endif

#ifndef __STDINT_LOADED
typedef unsigned int uintmax_t;
#endif

enum flags {
	FL_SPLAT = 0x01,	/* Drop the value, do not assign */
	FL_INV   = 0x02,	/* Character-set with inverse */
	FL_WIDTH = 0x04,	/* Field width specified */
	FL_MINUS = 0x08,	/* Negative number */
};

enum ranks {
	rank_char     = -2,
	rank_short    = -1,
	rank_int      = 0,
	rank_long     = 1,
	rank_longlong = 2,
	rank_ptr      = INT_MAX	/* Special value used for pointers */
};

#define MIN_RANK	rank_char
#define MAX_RANK	rank_longlong

#define INTMAX_RANK	rank_longlong
#define SIZE_T_RANK	rank_long
#define PTRDIFF_T_RANK	rank_long

enum bail {
	bail_none = 0,		/* No error condition */
	bail_eof,		/* Hit EOF */
	bail_err		/* Conversion mismatch */
};



static inline int digitval(int ch)
{
    	if (ch >= '0' && ch <= '9') {
		return ch - '0';
	} else if (ch >= 'A' && ch <= 'Z') {
		return ch - 'A' + 10;
	} else if (ch >= 'a' && ch <= 'z') {
		return ch - 'a' + 10;
	} else {
		return -1;
	}
}

static uintmax_t strntoumax(const char *nptr, char **endptr, int base, size_t n)
{
	int minus = 0;
	uintmax_t v = 0;
	int d;

	while (n && isspace((unsigned char)*nptr)) {
		nptr++;
		n--;
	}

	/* Single optional + or - */
	if (n) {
		char c = *nptr;
		if (c == '-' || c == '+') {
			minus = (c == '-');
			nptr++;
			n--;
		}
	}

	if (base == 0) {
		if (n >= 2 && nptr[0] == '0' &&
		    (nptr[1] == 'x' || nptr[1] == 'X')) {
			n -= 2;
			nptr += 2;
			base = 16;
		} else if (n >= 1 && nptr[0] == '0') {
			n--;
			nptr++;
			base = 8;
		} else {
			base = 10;
		}
	} else if (base == 16) {
		if (n >= 2 && nptr[0] == '0' &&
		    (nptr[1] == 'x' || nptr[1] == 'X')) {
			n -= 2;
			nptr += 2;
		}
	}

	while (n && (d = digitval(*nptr)) >= 0 && d < base) {
		v = v * base + d;
		n--;
		nptr++;
	}

	if (endptr)
		*endptr = (char *)nptr;

	return minus ? -v : v;
}


static inline const char *skipspace(const char *p)
{
	while (isspace((unsigned char)*p))
		p++;
	return p;
}

#undef set_bit
static inline void set_bit(unsigned long *bitmap, unsigned int bit)
{
	bitmap[bit / LONG_BIT] |= 1UL << (bit % LONG_BIT);
}

#undef test_bit
static inline int test_bit(unsigned long *bitmap, unsigned int bit)
{
	return (int)(bitmap[bit / LONG_BIT] >> (bit % LONG_BIT)) & 1;
}

int rsscanf(const char *buffer, const char *format, char ***argv)
{
	const char *p = format;
	char ch;
	unsigned char uc;
	const char *q = buffer;
	const char *qq;
	uintmax_t val = 0;
	int rank = rank_int;	/* Default rank */
	unsigned int width = UINT_MAX;
	int base;
	enum flags flags = 0;
	enum {
		st_normal,	/* Ground state */
		st_flags,	/* Special flags */
		st_width,	/* Field width */
		st_modifiers,	/* Length or conversion modifiers */
		st_match_init,	/* Initial state of %[ sequence */
		st_match,	/* Main state of %[ sequence */
		st_match_range,	/* After - in a %[ sequence */
	} state = st_normal;
	char *sarg = NULL;	/* %s %c or %[ string argument */
	enum bail bail = bail_none;
	int sign;
	int converted = 0;	/* Successful conversions */
	unsigned long matchmap[((1 << CHAR_BIT) + (LONG_BIT - 1)) / LONG_BIT];
	int matchinv = 0;	/* Is match map inverted? */
	unsigned char range_start = 0;
	(void)sign;
	char tmp[256];

	*argv = NULL;

	while ((ch = *p++) && !bail) {
		switch (state) {
		case st_normal:
			if (ch == '%') {
				state = st_flags;
				flags = 0;
				rank = rank_int;
				width = UINT_MAX;
			} else if (isspace((unsigned char)ch)) {
				q = skipspace(q);
			} else {
				if (*q == ch)
					q++;
				else
					bail = bail_err; /* Match failure */
			}
			break;

		case st_flags:
			switch (ch) {
			case '*':
				flags |= FL_SPLAT;
				break;
			case '0':
			case '1':
			case '2':
			case '3':
			case '4':
			case '5':
			case '6':
			case '7':
			case '8':
			case '9':
				width = (ch - '0');
				state = st_width;
				flags |= FL_WIDTH;
				break;
			default:
				state = st_modifiers;
				p--;	/* Process this character again */
				break;
			}
			break;

		case st_width:
			if (ch >= '0' && ch <= '9') {
				width = width * 10 + (ch - '0');
			} else {
				state = st_modifiers;
				p--;	/* Process this character again */
			}
			break;

		case st_modifiers:
			switch (ch) {
				/* Length modifiers - nonterminal sequences */
			case 'h':
				rank--;	/* Shorter rank */
				break;
			case 'l':
				rank++;	/* Longer rank */
				break;
			case 'j':
				rank = INTMAX_RANK;
				break;
			case 'z':
				rank = SIZE_T_RANK;
				break;
			case 't':
				rank = PTRDIFF_T_RANK;
				break;
			case 'L':
			case 'q':
				rank = rank_longlong;	/* long double/long long */
				break;

			default:
				/* Output modifiers - terminal sequences */
				/* Next state will be normal */
				state = st_normal;

				/* Canonicalize rank */
				if (rank < MIN_RANK)
					rank = MIN_RANK;
				else if (rank > MAX_RANK)
					rank = MAX_RANK;

				switch (ch) {
				case 'P':	/* Upper case pointer */
				case 'p':	/* Pointer */
					rank = rank_ptr;
					base = 0;
					sign = 0;
					goto scan_int;

				case 'i':	/* Base-independent integer */
					base = 0;
					sign = 1;
					goto scan_int;

				case 'd':	/* Decimal integer */
					base = 10;
					sign = 1;
					goto scan_int;

				case 'o':	/* Octal integer */
					base = 8;
					sign = 0;
					goto scan_int;

				case 'u':	/* Unsigned decimal integer */
					base = 10;
					sign = 0;
					goto scan_int;

				case 'x':	/* Hexadecimal integer */
				case 'X':
					base = 16;
					sign = 0;
					goto scan_int;

				case 'n':	/* # of characters consumed */
					val = (q - buffer);
					goto set_integer;

				      scan_int:
					q = skipspace(q);
					if (!*q) {
						bail = bail_eof;
						break;
					}
					val =
					    strntoumax(q, (char **)&qq, base,
						       width);
					if (qq == q) {
						bail = bail_err;
						break;
					}
					q = qq;
					if (!(flags & FL_SPLAT))
						converted++;
					/* fall through */

				      set_integer:
					if (!(flags & FL_SPLAT)) {
						switch (rank) {
						case rank_char:
							sprintf(tmp, "%c", *(char*)&val);
							*argv = realloc(*argv, (converted + 1) * sizeof(char *));
							(*argv)[converted - 1] = strdup(tmp);
							break;
						case rank_short:
							sprintf(tmp, "%d", *(short*)&val);
							*argv = realloc(*argv, (converted + 1) * sizeof(char *));
							(*argv)[converted - 1] = strdup(tmp);
							break;
						case rank_int:
							sprintf(tmp, "%d", *(int*)&val);
							*argv = realloc(*argv, (converted + 1) * sizeof(char *));
							(*argv)[converted - 1] = strdup(tmp);
							break;
						case rank_long:
							sprintf(tmp, "%ld", *(long*)&val);
							*argv = realloc(*argv, (converted + 1) * sizeof(char *));
							(*argv)[converted - 1] = strdup(tmp);
							break;
						case rank_longlong:
							sprintf(tmp, "%lld", *(long long int*)&val);
							*argv = realloc(*argv, (converted + 1) * sizeof(char *));
							(*argv)[converted - 1] = strdup(tmp);
							break;
						case rank_ptr:
							sprintf(tmp, "%llx", *(void**)&val);
							*argv = realloc(*argv, (converted + 1) * sizeof(char *));
							(*argv)[converted - 1] = strdup(tmp);
							break;
						}
					}
					break;

				case 'c':	/* Character */
					/* Default width == 1 */
					width = (flags & FL_WIDTH) ? width : 1;
					if (flags & FL_SPLAT) {
						while (width--) {
							if (!*q) {
								bail = bail_eof;
								break;
							}
						}
					} else {
						sarg = tmp;
						while (width--) {
							if (!*q) {
								bail = bail_eof;
								break;
							}
							*sarg++ = *q++;
						}
						if (!bail) {
							converted++;
							*sarg = '\0';
							*argv = realloc(*argv, (converted + 1) * sizeof(char *));
							(*argv)[converted - 1] = strdup(tmp);
						}
					}
					break;

				case 's':	/* String */
					uc = 1;	/* Anything nonzero */
					if (flags & FL_SPLAT) {
						while (width-- && (uc = *q) &&
						       !isspace(uc)) {
							q++;
						}
					} else {
						char *sp;
						sp = sarg = tmp;
						while (width-- && (uc = *q) &&
						       !isspace(uc)) {
							*sp++ = uc;
							q++;
						}
						if (sarg != sp) {
							/* Terminate output */
							*sp = '\0';
							converted++;
							*argv = realloc(*argv, (converted + 1) * sizeof(char *));
							(*argv)[converted - 1] = strdup(tmp);
						}
					}
					if (!uc)
						bail = bail_eof;
					break;

				case '[':	/* Character range */
					sarg = (flags & FL_SPLAT) ? NULL
						: tmp;
					state = st_match_init;
					matchinv = 0;
					memset(matchmap, 0, sizeof matchmap);
					break;

				case '%':	/* %% sequence */
					if (*q == '%')
						q++;
					else
						bail = bail_err;
					break;

				default:	/* Anything else */
					/* Unknown sequence */
					bail = bail_err;
					break;
				}
			}
			break;

		case st_match_init:	/* Initial state for %[ match */
			if (ch == '^' && !(flags & FL_INV)) {
				matchinv = 1;
			} else {
				set_bit(matchmap, (unsigned char)ch);
				state = st_match;
			}
			break;

		case st_match:	/* Main state for %[ match */
			if (ch == ']') {
				goto match_run;
			} else if (ch == '-') {
				range_start = (unsigned char)ch;
				state = st_match_range;
			} else {
				set_bit(matchmap, (unsigned char)ch);
			}
			break;

		case st_match_range:	/* %[ match after - */
			if (ch == ']') {
				/* - was last character */
				set_bit(matchmap, (unsigned char)'-');
				goto match_run;
			} else {
				int i;
				for (i = range_start; i < (unsigned char)ch;
				     i++)
					set_bit(matchmap, i);
				state = st_match;
			}
			break;

		      match_run:	/* Match expression finished */
			qq = q;
			uc = 1;	/* Anything nonzero */
			while (width && (uc = *q)
			       && test_bit(matchmap, uc)^matchinv) {
				if (sarg)
					*sarg++ = uc;
				q++;
			}
			if (q != qq && sarg) {
				*sarg = '\0';
				converted++;
				*argv = realloc(*argv, (converted + 1) * sizeof(char *));
				(*argv)[converted - 1] = strdup(tmp);
			} else {
				bail = bail_err;
			}
			if (!uc)
				bail = bail_eof;
			break;
		}
	}

	if (converted) {
		(*argv)[converted] = NULL;
	}

	if (bail == bail_eof && !converted) {
		converted = -1;	/* Return EOF (-1) */
	}


	return converted;
}

