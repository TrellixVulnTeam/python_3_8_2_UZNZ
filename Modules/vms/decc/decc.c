#define __NEW_STARLET 1
#include <stdio.h>
#include <string.h>
#include <lib$routines.h>
#include <starlet.h>
#include <descrip.h>
#include <ssdef.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <assert.h>
#include <dlfcn.h>
#include <stdarg.h>

#include "decc.h"

#ifndef adc_Assert
#define adc_Assert(x) \
    do { \
        if ((!(x))) { \
            fprintf (stderr, "Assertion failed: %s (%s: %d)\n", #x, __FILE__, __LINE__); \
            abort(); \
        } \
    } while (0)
#endif

extern unsigned int decc$fix_time(long long *);

unsigned int _fix_time(long long vms_time)
{
    return (decc$fix_time(&vms_time));
}


static long long epoch = 0;

#define UNIX_EPOCH "01-JAN-1970 00:00:00.00"
#define FAC 10000000L

static int offset()
{
    time_t gmt, rawtime = time(NULL);
    struct tm *ptm;

    struct tm gbuf;
    ptm = gmtime_r(&rawtime, &gbuf);
    ptm->tm_isdst = -1;
    gmt = mktime(ptm);

    return ((int) difftime(rawtime, gmt));
}

unsigned int _unixtime(long long dt)
{
    unsigned int sec;
    __int64 diff;

    if (epoch == 0)  {
        struct dsc$descriptor_s epoch_dsc;

        epoch_dsc.dsc$w_length = strlen(UNIX_EPOCH);
        epoch_dsc.dsc$b_class = DSC$K_CLASS_S;
        epoch_dsc.dsc$b_dtype = DSC$K_DTYPE_T;
        epoch_dsc.dsc$a_pointer = UNIX_EPOCH;

        sys$bintim(&epoch_dsc, (struct _generic_64 *) &epoch);
    }

    diff = dt - epoch;
    sec = diff / FAC - offset();
    return (sec);
}



long long _vmstime(unsigned int dt)
{
    long long val;
    long long tmp;

    if (epoch == 0)  {
        struct dsc$descriptor_s epoch_dsc;

        epoch_dsc.dsc$w_length = strlen(UNIX_EPOCH);
        epoch_dsc.dsc$b_class = DSC$K_CLASS_S;
        epoch_dsc.dsc$b_dtype = DSC$K_DTYPE_T;
        epoch_dsc.dsc$a_pointer = UNIX_EPOCH;

        sys$bintim(&epoch_dsc, (struct _generic_64 *) &epoch);
    }

    tmp = dt;
    val = epoch + (tmp * FAC);

    return (val);
}


extern int decc$from_vms(const char *, int (*)(char *, void *), int, ...);
extern int decc$to_vms(const char *, int (*)(char *, int, void *), int, int, ...);

typedef struct {
    int     len;
    int     cap;
    char**  buf;
} _simple_arr;

static int cb_from_vms(char *name, void *user_data)
{
    _simple_arr *parr = (_simple_arr *) user_data;
    assert(parr);
    if (parr->len + 1 >= parr->cap ) {
        parr->cap += 8;
        parr->buf = realloc(parr->buf, parr->cap * sizeof(char*));
    }
    parr->buf[parr->len] = strdup(name);
    assert(parr->buf[parr->len]);
    ++parr->len;
    parr->buf[parr->len] = NULL;
    return (1);
}


char **_from_vms(char *path, int wild_flag)
{
    _simple_arr arr;
    arr.len = 0;
    arr.cap = 8;
    arr.buf = malloc(arr.cap * sizeof(char*));
    arr.buf[arr.len] = NULL;

    assert(path);
    int num_files = decc$from_vms(path, cb_from_vms, wild_flag, &arr);
    return (arr.buf);
}


static int cb_to_vms(char *name, int flag, void *user_data)
{
    _simple_arr *parr = (_simple_arr *) user_data;
    assert(parr);
    if (parr->len + 1 >= parr->cap ) {
        parr->cap += 8;
        parr->buf = realloc(parr->buf, parr->cap * sizeof(char*));
    }
    parr->buf[parr->len] = strdup(name);
    assert(parr->buf[parr->len]);
    ++parr->len;
    parr->buf[parr->len] = NULL;
    return (1);
}

char **_to_vms(char *path, int allow_wild, int no_directory)
{
    _simple_arr arr;
    arr.len = 0;
    arr.cap = 8;
    arr.buf = malloc(arr.cap * sizeof(char*));
    arr.buf[arr.len] = NULL;

    assert(path);
    decc$to_vms(path, cb_to_vms, allow_wild, no_directory, &arr);
    return (arr.buf);
}


char *_getenv(char *name, char *def)
{
    char *tmp, *val = NULL;

    adc_Assert(name);
    val = getenv(name);

    if (val == NULL && def != NULL) {
       val = def;
    }

    if (val) {
        adc_Assert((tmp = strdup(val)));
    } else {
        tmp = NULL;
    }

    return (tmp);
}


long _sysconf(int name)
{
    return (sysconf(name));
}


int _sleep(unsigned int nsec)
{
    return (sleep(nsec));
}

int _dlopen_test(char *name) {
    void *handle = dlopen(name, 0);
    if (handle) {
        dlclose(handle);
        return 1;
    }
    return 0;
}

int _get_symbol(char *name, char** value) {
    struct dsc$descriptor_s symbol_name;
    symbol_name.dsc$w_length = strlen(name);
    symbol_name.dsc$b_class = DSC$K_CLASS_S;
    symbol_name.dsc$b_dtype = DSC$K_DTYPE_T;
    symbol_name.dsc$a_pointer = name;

    char buffer[256];
    buffer[0] = 0;
    struct dsc$descriptor_s symbol_value;
    symbol_value.dsc$w_length = 255;
    symbol_value.dsc$b_class = DSC$K_CLASS_S;
    symbol_value.dsc$b_dtype = DSC$K_DTYPE_T;
    symbol_value.dsc$a_pointer = buffer;

    short result_len = 0;
    int status = lib$get_symbol(&symbol_name, &symbol_value, &result_len);
    buffer[result_len] = 0;
    *value = strdup(buffer);
    return status;
}

void *_fopen(char *path, char *mode, ...)
{
    va_list ap;
    int n;
    char **arr;
    unsigned int *argv;
    int argc;
    FILE *fp = NULL;

    if (!path) {
        return NULL;
    }
    if (!mode) {
        return NULL;
    }

    va_count(argc);
    n = 0;

    if (argc == 3) {
        va_start(ap, mode);
        arr = (char **) va_arg(ap, char **);
        va_end(ap);
        while (arr[n]) {
            n++;
        }
    }

    argc = n + 2;
    argv = malloc(argc * sizeof(unsigned int));
    adc_Assert(argv);

    argv[0] = argc;
    argv[1] = (unsigned int) path;
    argv[2] = (unsigned int) mode;

    if (argc == 3) {
        n = 0;
        while (arr[n]) {
            argv[n + 3] = (unsigned int) arr[n];
            n++;
        }
    }

    fp = (FILE *) lib$callg(argv, (int (*)(void)) fopen);
    free(argv);
    return (fp);
}


int _fclose(void *fp)
{
    if (!fp) {
        return -1;
    }
    return (fclose(fp));
}


int _fileno(void *fp)
{
    if (!fp) {
        return -1;
    }
    return (fileno(fp));
}


int _write(int fd, const char *buf, int len)
{
    return (write(fd, buf, len));
}


#ifndef MAX_REC_LEN
#define MAX_REC_LEN 32000
#endif

char *_fgets(void *fp, int len)
{
    char *tmp;

    if (!fp) {
        return NULL;
    }

    if (len < 1 || len > MAX_REC_LEN) {
        len = MAX_REC_LEN;
    }

    tmp = malloc(len);
    adc_Assert(tmp);

    if (fgets(tmp, len, fp) == NULL) {
        free(tmp);
        tmp = NULL;
    }

    return (tmp);
}


int _feof(void *fp)
{
    if (!fp) {
        return -1;
    }
    return (feof(fp));
}


int _ferror(void *fp)
{
    if (!fp) {
        return -1;
    }
    return (ferror(fp));
}
