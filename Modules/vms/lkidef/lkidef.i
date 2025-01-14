%module lkidef

%constant int LKI_K_LENGTH = 24;
%constant int LKI_C_LENGTH = 24;
%constant int LKI_K_BR_LENGTH = 56;
%constant int LKI_C_BR_LENGTH = 56;
%constant int LKI_S_LKIDEF = 56;
%constant int LKI_S_RQSTART = 8;
%constant int LKI_S_RQLENGTH = 8;
%constant int LKI_S_GRSTART = 8;
%constant int LKI_S_GRLENGTH = 8;
%constant int LKI_M_SYSNAM = 0x80000000L;
%constant int LKI_S_NAMSPACE = 4;
%constant int LKI_S_STATEF = 3;
%constant int LKIUSR_K_LENGTH = 20;
%constant int LKIUSR_C_LENGTH = 20;
%constant int LKIUSR_K_BLOCKER_START = 20;
%constant int LKIUSR_S_LKIUSRDEF = 20;
%constant int LKIUSR_S_START = 8;
%constant int LKIUSR_S_LENGTH = 8;
%constant int LKI__RNG_S_RNGDEF = 32;
%constant int LKI__RNG_S_RQSTART = 8;
%constant int LKI__RNG_S_RQLENGTH = 8;
%constant int LKI__RNG_S_GRSTART = 8;
%constant int LKI__RNG_S_GRLENGTH = 8;
%constant int LKI_C_GRANTED = 1;
%constant int LKI_C_CONVERT = 0;
%constant int LKI_C_WAITING = -1;
%constant int LKI_C_RETRY = -2;
%constant int LKI_C_SCSWAIT = -3;
%constant int LKI_C_RSPNOTQED = -4;
%constant int LKI_C_RSPQUEUED = -5;
%constant int LKI_C_RSPGRANTD = -6;
%constant int LKI_C_RSPDOLOCL = -7;
%constant int LKI_C_RSPRESEND = -8;
%constant int LKI_C_LKBTYPE = 1;
%constant int LKI_C_RSBTYPE = 2;
%constant int LKI_C_LISTEND = 0;
%constant int LKI__PID = 256;
%constant int LKI__STATE = 257;
%constant int LKI__PARENT = 258;
%constant int LKI__LCKREFCNT = 259;
%constant int LKI__LOCKID = 260;
%constant int LKI__REMLKID = 261;
%constant int LKI__MSTLKID = 262;
%constant int LKI__LKID = 263;
%constant int LKI__CSID = 264;
%constant int LKI__BRL = 265;
%constant int LKI__RANGE = 266;
%constant int LKI__LASTLKB = 267;
%constant int LKI__NAMSPACE = 512;
%constant int LKI__RESNAM = 513;
%constant int LKI__RSBREFCNT = 514;
%constant int LKI__VALBLK = 515;
%constant int LKI__SYSTEM = 516;
%constant int LKI__LCKCOUNT = 517;
%constant int LKI__BLOCKEDBY = 518;
%constant int LKI__BLOCKING = 519;
%constant int LKI__LOCKS = 520;
%constant int LKI__CVTCOUNT = 521;
%constant int LKI__WAITCOUNT = 522;
%constant int LKI__GRANTCOUNT = 523;
%constant int LKI__MSTCSID = 524;
%constant int LKI__VALBLKST = 525;
%constant int LKI__BLOCKEDBY_BR = 526;
%constant int LKI__BLOCKING_BR = 527;
%constant int LKI__LOCKS_BR = 528;
%constant int LKI__BLOCKER_BR = 529;
%constant int LKI__XVALBLK = 530;
%constant int LKI__XVALNOTVALID = 531;
%constant int LKI__LASTRSB = 532;
%constant int LKISND_K_HDRLEN = 16;
%constant int LKISND_C_HDRLEN = 16;
%constant int LKISND_S_LKISNDDEF = 16;
