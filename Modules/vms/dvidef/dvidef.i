%module dvidef

%constant int DVI__DEVCHAR = 2;
%constant int DVI__DEVCLASS = 4;
%constant int DVI__DEVTYPE = 6;
%constant int DVI__DEVBUFSIZ = 8;
%constant int DVI__DEVDEPEND = 10;
%constant int DVI__UNIT = 12;
%constant int DVI__PID = 14;
%constant int DVI__OWNUIC = 16;
%constant int DVI__VPROT = 18;
%constant int DVI__ERRCNT = 20;
%constant int DVI__OPCNT = 22;
%constant int DVI__RECSIZ = 24;
%constant int DVI__MAXBLOCK = 26;
%constant int DVI__DEVDEPEND2 = 28;
%constant int DVI__REFCNT = 30;
%constant int DVI__DEVNAM = 32;
%constant int DVI__VOLNAM = 34;
%constant int DVI__SECTORS = 36;
%constant int DVI__TRACKS = 38;
%constant int DVI__CYLINDERS = 40;
%constant int DVI__FREEBLOCKS = 42;
%constant int DVI__LOGVOLNAM = 44;
%constant int DVI__VOLNUMBER = 46;
%constant int DVI__VOLCOUNT = 48;
%constant int DVI__ROOTDEVNAM = 50;
%constant int DVI__NEXTDEVNAM = 52;
%constant int DVI__TRANSCNT = 54;
%constant int DVI__MOUNTCNT = 56;
%constant int DVI__CLUSTER = 58;
%constant int DVI__MAXFILES = 60;
%constant int DVI__SERIALNUM = 62;
%constant int DVI__ACPPID = 64;
%constant int DVI__ACPTYPE = 66;
%constant int DVI__CONCEALED = 68;
%constant int DVI__REC = 70;
%constant int DVI__CCL = 72;
%constant int DVI__TRM = 74;
%constant int DVI__DIR = 76;
%constant int DVI__SDI = 78;
%constant int DVI__SQD = 80;
%constant int DVI__SPL = 82;
%constant int DVI__OPR = 84;
%constant int DVI__RCT = 86;
%constant int DVI__NET = 88;
%constant int DVI__FOD = 90;
%constant int DVI__DUA = 92;
%constant int DVI__SHR = 94;
%constant int DVI__GEN = 96;
%constant int DVI__AVL = 98;
%constant int DVI__MNT = 100;
%constant int DVI__MBX = 102;
%constant int DVI__DMT = 104;
%constant int DVI__ELG = 106;
%constant int DVI__ALL = 108;
%constant int DVI__FOR = 110;
%constant int DVI__SWL = 112;
%constant int DVI__IDV = 114;
%constant int DVI__ODV = 116;
%constant int DVI__RND = 118;
%constant int DVI__RTM = 120;
%constant int DVI__RCK = 122;
%constant int DVI__WCK = 124;
%constant int DVI__TT_PASSALL = 126;
%constant int DVI__TT_NOECHO = 128;
%constant int DVI__TT_NOTYPEAHD = 130;
%constant int DVI__TT_ESCAPE = 132;
%constant int DVI__TT_HOSTSYNC = 134;
%constant int DVI__TT_TTSYNC = 136;
%constant int DVI__TT_SCRIPT = 138;
%constant int DVI__TT_LOWER = 140;
%constant int DVI__TT_MECHTAB = 142;
%constant int DVI__TT_WRAP = 144;
%constant int DVI__TT_CRFILL = 146;
%constant int DVI__TT_LFFILL = 148;
%constant int DVI__TT_SCOPE = 150;
%constant int DVI__TT_REMOTE = 152;
%constant int DVI__TT_EIGHTBIT = 154;
%constant int DVI__TT_MBXDSABL = 156;
%constant int DVI__TT_NOBRDCST = 158;
%constant int DVI__TT_READSYNC = 160;
%constant int DVI__TT_MECHFORM = 162;
%constant int DVI__TT_HALFDUP = 164;
%constant int DVI__TT_MODEM = 166;
%constant int DVI__TT_OPER = 168;
%constant int DVI__TT_PAGE = 170;
%constant int DVI__TT_LOCALECHO = 172;
%constant int DVI__TT_AUTOBAUD = 174;
%constant int DVI__TT_HANGUP = 176;
%constant int DVI__TT_MODHANGUP = 178;
%constant int DVI__TT_BRDCSTMBX = 180;
%constant int DVI__TT_DMA = 182;
%constant int DVI__TT_ALTYPEAHD = 184;
%constant int DVI__TT_SETSPEED = 186;
%constant int DVI__TT_DCL_MAILBX = 188;
%constant int DVI__TT_EDITING = 190;
%constant int DVI__TT_INSERT = 192;
%constant int DVI__TT_FALLBACK = 194;
%constant int DVI__TT_DIALUP = 196;
%constant int DVI__TT_SECURE = 198;
%constant int DVI__TT_DISCONNECT = 200;
%constant int DVI__TT_PASTHRU = 202;
%constant int DVI__TT_SIXEL = 204;
%constant int DVI__TT_DRCS = 206;
%constant int DVI__TT_PRINTER = 208;
%constant int DVI__TT_APP_KEYPAD = 210;
%constant int DVI__TT_SYSPWD = 212;
%constant int DVI__TT_ANSICRT = 214;
%constant int DVI__TT_REGIS = 216;
%constant int DVI__TT_BLOCK = 218;
%constant int DVI__TT_AVO = 220;
%constant int DVI__TT_EDIT = 222;
%constant int DVI__TT_DECCRT = 224;
%constant int DVI__STS = 226;
%constant int DVI__DEVSTS = 228;
%constant int DVI__DEVCHAR2 = 230;
%constant int DVI__FULLDEVNAM = 232;
%constant int DVI__LOCKID = 234;
%constant int DVI__ALLDEVNAM = 236;
%constant int DVI__VOLSETMEM = 238;
%constant int DVI__DEVLOCKNAM = 240;
%constant int DVI__ALLOCLASS = 242;
%constant int DVI__ALT_HOST_AVAIL = 244;
%constant int DVI__ALT_HOST_NAME = 246;
%constant int DVI__ALT_HOST_TYPE = 248;
%constant int DVI__HOST_AVAIL = 250;
%constant int DVI__HOST_COUNT = 252;
%constant int DVI__HOST_NAME = 254;
%constant int DVI__HOST_TYPE = 256;
%constant int DVI__REMOTE_DEVICE = 258;
%constant int DVI__SERVED_DEVICE = 260;
%constant int DVI__SHDW_CATCHUP_COPYING = 262;
%constant int DVI__SHDW_MASTER = 264;
%constant int DVI__SHDW_MASTER_NAME = 266;
%constant int DVI__SHDW_MEMBER = 268;
%constant int DVI__SHDW_MERGE_COPYING = 270;
%constant int DVI__SHDW_NEXT_MBR_NAME = 272;
%constant int DVI__TT_PHYDEVNAM = 274;
%constant int DVI__TT_DECCRT2 = 276;
%constant int DVI__MEDIA_NAME = 278;
%constant int DVI__MEDIA_TYPE = 280;
%constant int DVI__MEDIA_ID = 282;
%constant int DVI__SHDW_FAILED_MEMBER = 284;
%constant int DVI__MSCP_UNIT_NUMBER = 286;
%constant int DVI__DISPLAY_DEVNAM = 288;
%constant int DVI__TT_ACCPORNAM = 290;
%constant int DVI__DEVDEPEND3 = 292;
%constant int DVI__TT_MULTISESSION = 294;
%constant int DVI__TT_DECCRT3 = 296;
%constant int DVI__SET_HOST_TERMINAL = 298;
%constant int DVI__DFS_ACCESS = 300;
%constant int DVI__DAPDEVNAM = 302;
%constant int DVI__TT_DECCRT4 = 304;
%constant int DVI__TT_CHARSET = 306;
%constant int DVI__TT_CS_KANA = 308;
%constant int DVI__TT_CS_KANJI = 310;
%constant int DVI__TT_CS_HANZI = 312;
%constant int DVI__TT_CS_HANGUL = 314;
%constant int DVI__TT_CS_HANYU = 316;
%constant int DVI__TT_CS_THAI = 318;
%constant int DVI__DEVDEPEND4 = 320;
%constant int DVI__DEVICE_TYPE_NAME = 322;
%constant int DVI__TT_ASIAN_MODE = 324;
%constant int DVI__PREFERRED_CPU = 326;
%constant int DVI__TT_DECCRT5 = 328;
%constant int DVI__TT_ANSI_COLOR = 330;
%constant int DVI__MT3_SUPPORTED = 332;
%constant int DVI__MT3_DENSITY = 334;
%constant int DVI__DRIVER_IMAGE_NAME = 336;
%constant int DVI__CLIENT_DEVICE = 338;
%constant int DVI__FC_PORT_NAME = 340;
%constant int DVI__FC_NODE_NAME = 342;
%constant int DVI__WWID = 344;
%constant int DVI__VOLCHAR = 346;
%constant int DVI__HBVS_MASTER_MEMBER = 348;
%constant int DVI__MULTIPATH = 350;
%constant int DVI__MPDEV_CURRENT_PATH = 352;
%constant int DVI__VOLSIZE = 354;
%constant int DVI__EXPSIZE = 356;
%constant int DVI__QLEN = 358;
%constant int DVI__SHDW_SITE = 360;
%constant int DVI__SHDW_MBR_COUNT = 362;
%constant int DVI__SHDW_DEVICE_COUNT = 364;
%constant int DVI__SHDW_MBR_READ_COST = 366;
%constant int DVI__SHDW_READ_SOURCE = 368;
%constant int DVI__SHDW_TIMEOUT = 370;
%constant int DVI__DVI_UNUSED_1 = 372;
%constant int DVI__SHDW_GENERATION = 374;
%constant int DVI__SHDW_STATUS = 376;
%constant int DVI__SHDW_MBR_COPY_DONE = 378;
%constant int DVI__SHDW_MBR_MERGE_DONE = 380;
%constant int DVI__SHDW_MINIMERGE_ENABLE = 382;
%constant int DVI__DVI_UNUSED_2 = 384;
%constant int DVI__SHDW_COPIER_NODE = 386;
%constant int DVI__SHDW_MASTER_MBR = 388;
%constant int DVI__MPDEV_AUTO_PATH_SW_CNT = 390;
%constant int DVI__MPDEV_MAN_PATH_SW_CNT = 392;
%constant int DVI__WRITETHRU_CACHE_ENABLED = 394;
%constant int DVI__NOCACHE_ON_VOLUME = 396;
%constant int DVI__MOUNTVER_ELIGIBLE = 398;
%constant int DVI__ERASE_ON_DELETE = 400;
%constant int DVI__NOHIGHWATER = 402;
%constant int DVI__NOSHARE_MOUNTED = 404;
%constant int DVI__CLUSLOCK = 406;
%constant int DVI__ODS2_SUBSET0 = 408;
%constant int DVI__PROT_SUBSYSTEM_ENABLED = 410;
%constant int DVI__ODS5 = 412;
%constant int DVI__ACCESSTIMES_RECORDED = 414;
%constant int DVI__HARDLINKS_SUPPORTED = 416;
%constant int DVI__SCSI_DEVICE_FIRMWARE_REV = 418;
%constant int DVI__TOTAL_PATH_COUNT = 420;
%constant int DVI__AVAILABLE_PATH_COUNT = 422;
%constant int DVI__VOLUME_EXTEND_QUANTITY = 424;
%constant int DVI__MOUNT_TIME = 426;
%constant int DVI__VOLUME_MOUNT_SYS = 428;
%constant int DVI__VOLUME_MOUNT_GROUP = 430;
%constant int DVI__PATH_AVAILABLE = 432;
%constant int DVI__PATH_USER_DISABLED = 434;
%constant int DVI__PATH_NOT_RESPONDING = 436;
%constant int DVI__PATH_POLL_ENABLED = 438;
%constant int DVI__MVSUPMSG = 440;
%constant int DVI__PATH_SWITCH_TO_TIME = 442;
%constant int DVI__PATH_SWITCH_FROM_TIME = 444;
%constant int DVI__ERROR_RESET_TIME = 446;
%constant int DVI__DEVICE_MAX_IO_SIZE = 448;
%constant int DVI__VOLUME_RETAIN_MAX = 450;
%constant int DVI__VOLUME_RETAIN_MIN = 452;
%constant int DVI__PREFERRED_CPU_BITMAP = 454;
%constant int DVI__MAILBOX_INITIAL_QUOTA = 456;
%constant int DVI__MAILBOX_BUFFER_QUOTA = 458;
%constant int DVI__VOLUME_WINDOW = 460;
%constant int DVI__VOLUME_SPOOLED_DEV_CNT = 462;
%constant int DVI__VOLUME_PENDING_WRITE_ERR = 464;
%constant int DVI__LAN_SPEED = 466;
%constant int DVI__LAN_LINK_UP = 468;
%constant int DVI__LAN_DEFAULT_MAC_ADDRESS = 470;
%constant int DVI__LAN_MAC_ADDRESS = 472;
%constant int DVI__LAN_FULL_DUPLEX = 474;
%constant int DVI__LAN_ALL_MULTICAST_MODE = 476;
%constant int DVI__LAN_PROMISCUOUS_MODE = 478;
%constant int DVI__LAN_JUMBO_FRAMES_ENABLED = 480;
%constant int DVI__LAN_AUTONEG_ENABLED = 482;
%constant int DVI__LAN_PROTOCOL_TYPE = 484;
%constant int DVI__LAN_PROTOCOL_NAME = 486;
%constant int DVI__LAN_LINK_STATE_VALID = 488;
%constant int DVI__FC_HBA_FIRMWARE_REV = 490;
%constant int DVI__ADAPTER_IDENT = 492;
%constant int DVI__MOUNTCNT_CLUSTER = 494;
%constant int DVI__SHDW_HBMM_RESET_COUNT = 496;
%constant int DVI__SHDW_HBMM_RESET_TIME = 498;
%constant int DVI__SPECIAL_FILES = 500;
%constant int DVI__NOXFCCACHE_ON_VOLUME = 502;
%constant int DVI__XFC_DEPOSING = 504;
%constant int DVI__SSD_USAGE_REMAINING = 506;
%constant int DVI__SSD_LIFE_REMAINING = 508;
%constant int DVI_M_SECONDARY = 0x1L;
%constant int DVI_M_NOREDIRECT = 0x8000L;
%constant int DVI_S_DVIDEF = 2;
%constant int DVI_S_ITEM_CODE = 14;
%constant int DVI_M_VOL_READDIR = 0xFL;
%constant int DVI_C_READDIR_NONE = 0;
%constant int DVI_C_READDIR_VIO = 1;
%constant int DVI_C_READDIR_IO = 2;
%constant int DVI_C_READDIR_ACP = 3;
%constant int DVI_M_VOL_LENGTH_HINT = 0x10L;
%constant int DVI_M_VOL_CACHING_ATTR = 0x20L;
%constant int DVI_M_VOL_ACCESS_DATE = 0x40L;
%constant int DVI_M_VOL_HARDLINK = 0x80L;
%constant int DVI_M_VOL_SET_SECURITY = 0x100L;
%constant int DVI_M_VOL_FID_TO_NAME = 0x200L;
%constant int DVI_M_VOL_ODS1_STYLE_PURGE = 0x400L;
%constant int DVI_M_VOL_SHARED_TRUNCATE = 0x800L;
%constant int DVI_M_VOL_WRITE_BARRIER = 0x1000L;
%constant int DVI_M_VOL_DIRSEQ_QIO = 0x2000L;
%constant int DVI_M_VOL_EFS = 0x4000L;
%constant int DVI_M_VOL_UCS2 = 0x8000L;
%constant int DVI_M_VOL_CASE_VARIANT = 0x10000L;
%constant int DVI_M_VOL_MODDATE = 0x20000L;
%constant int DVI_M_VOL_SPECIAL_FILE = 0x40000L;
%constant int DVI_M_VOL_SSIO = 0x80000L;
%constant int DVI_M_VOL_LOOKUP_SPECIAL = 0x100000L;
%constant int DVI_S_DVIVOLDEF = 16;
%constant int DVI_S_VOL_READDIR = 4;
%constant int DVI_C_SECONDARY = 1;
%constant int DVI_C_ACP_F11V1 = 1;
%constant int DVI_C_ACP_F11V2 = 2;
%constant int DVI_C_ACP_MTA = 3;
%constant int DVI_C_ACP_NET = 4;
%constant int DVI_C_ACP_REM = 5;
%constant int DVI_C_ACP_HBS = 6;
%constant int DVI_C_ACP_F11V3 = 7;
%constant int DVI_C_ACP_F11V4 = 8;
%constant int DVI_C_ACP_F64 = 9;
%constant int DVI_C_ACP_UCX = 10;
%constant int DVI_C_ACP_F11V5 = 11;
%constant int DVI_C_ACP_F11V6 = 12;
%constant int DVI_C_ACP_HBVS = 13;