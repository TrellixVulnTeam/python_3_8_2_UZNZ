%module kgbdef

%constant int KGB_M_RESOURCE = 0x1L;
%constant int KGB_M_DYNAMIC = 0x2L;
%constant int KGB_M_NOACCESS = 0x4L;
%constant int KGB_M_SUBSYSTEM = 0x8L;
%constant int KGB_M_IMPERSONATE = 0x10L;
%constant int KGB_M_HOLDER_HIDDEN = 0x20L;
%constant int KGB_M_NAME_HIDDEN = 0x40L;
%constant int KGB_K_HOLD_RECORD = 16;
%constant int KGB_K_IDENT_RECORD = 48;
%constant int KGB_K_LEVEL1 = 257;
%constant int KGB_K_MAINT_RECORD = 64;
%constant int KGB_K_NUMBER_OF_ATTRIBUTES = 7;
%constant int KGB_S_KGBDEF = 64;
%constant int KGB_S_HOLDER = 8;
%constant int KGB_S_NAME = 32;
%constant int KGB_S_SYS_ID = 8;
%constant int KGB_K_BATCH_ID = -2147483647;
%constant int KGB_K_DIALUP_ID = -2147483646;
%constant int KGB_K_INTERACTIVE_ID = -2147483645;
%constant int KGB_K_LOCAL_ID = -2147483644;
%constant int KGB_K_NETWORK_ID = -2147483643;
%constant int KGB_K_REMOTE_ID = -2147483642;
%constant int KGB_K_DECWINDOWS_ID = -2147483641;
%constant int KGB_K_BOBUSER_ID = -2147483640;
%constant int KGB_K_MRES_USER_ID = -2147483639;
%constant int KGB_K_SAT_ACCESS_ID = -2147483638;
%constant int KGB_K_LAST_ENV_ID = -2147483637;
%constant int KGB_K_BASE_ENV_ID = -2147483647;
%constant int KGB_K_NUMBER_OF_ENV_IDS = 10;
%constant int KGB_K_RESTRICTED_RANGE = -2147418112;
%constant int KGB_K_SEC_LEVEL_BASE = -2147482648;
%constant int KGB_K_INT_LEVEL_BASE = -2147482392;
%constant int KGB_K_SEC_CATEGORY_BASE = -2147482136;
%constant int KGB_K_INT_CATEGORY_BASE = -2147482072;
%constant int KGB_K_SEC_ACCESS_CLASS_BASE = -2147482648;
%constant int KGB_K_SEC_ACCESS_CLASS_END = -2147482008;
%constant int KGB_K_PROCESS = 0;
%constant int KGB_K_SYSTEM = 1;
%constant int KGB_K_EXTENDED = 2;
%constant int KGB_K_IMAGE = 3;
%constant int KGB_K_MAX_SEG = 4;
%constant int KGB_K_SUBSYSTEM = 3;
