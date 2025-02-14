%module regdef

%constant int REG_FC_CLOSE_KEY = 1;
%constant int REG_FC_CREATE_KEY = 2;
%constant int REG_FC_DELETE_KEY = 3;
%constant int REG_FC_DELETE_VALUE = 4;
%constant int REG_FC_ENUM_KEY = 5;
%constant int REG_FC_ENUM_VALUE = 6;
%constant int REG_FC_FLUSH_KEY = 7;
%constant int REG_FC_LOAD_KEY = 8;
%constant int REG_FC_MODIFY_KEY = 9;
%constant int REG_FC_MODIFY_TREE_KEY = 10;
%constant int REG_FC_NOTIFY_CHANGE_KEY_VALUE = 11;
%constant int REG_FC_OPEN_KEY = 12;
%constant int REG_FC_QUERY_KEY = 13;
%constant int REG_FC_QUERY_VALUE = 14;
%constant int REG_FC_REPLACE_KEY = 15;
%constant int REG_FC_RESTORE_KEY = 16;
%constant int REG_FC_SAVE_KEY = 17;
%constant int REG_FC_SEARCH_TREE_DATA = 18;
%constant int REG_FC_SEARCH_TREE_KEY = 19;
%constant int REG_FC_SEARCH_TREE_VALUE = 20;
%constant int REG_FC_SET_VALUE = 21;
%constant int REG_FC_UNLOAD_KEY = 22;
%constant int REG_FC_GET_KEY_SECURITY = 23;
%constant int REG_FC_SET_KEY_SECURITY = 24;
%constant int REG_FC_GET_PERFORMANCE = 25;
%constant int REG_FC_GET_FILE_INFO = 26;
%constant int REG_FC_GET_FILE_UPDATE = 27;
%constant int REG_FC_CREATE_DATABASE = 28;
%constant int REG_FC_MAKE_SNAPSHOT = 29;
%constant int REG_FC_ARCHIVE = 30;
%constant int REG_FC_LAST = 31;
%constant int REG_M_UNICODE_STRING = 8192;
%constant int REG__TERMINATOR = 0;
%constant int REG__SEPARATOR = 1;
%constant int REG__SECPROFILE = 514;
%constant int REG__REQUEST = 515;
%constant int REG__ACMODE = 1284;
%constant int REG__ACTIONCODE = 1285;
%constant int REG__CACHEACTION = 1286;
%constant int REG__CANCELNOTIFICATION = 519;
%constant int REG__CLASSNAME = 264;
%constant int REG__CLASSNAMEMAX = 1289;
%constant int REG__CLASSNAMESIZE = 1290;
%constant int REG__DATAFLAGS = 1547;
%constant int REG__DATATYPE = 1292;
%constant int REG__DISPOSITION = 1293;
%constant int REG__FILEINFODATA = 526;
%constant int REG__FILELOAD = 1807;
%constant int REG__FILESAVE = 1808;
%constant int REG__FILEUPDATEDATA = 529;
%constant int REG__FLAGOPCODE = 1298;
%constant int REG__FLAGSUBKEY = 1299;
%constant int REG__KEYID = 1300;
%constant int REG__KEYID_INTERNAL = 533;
%constant int REG__KEYFLAGS = 1302;
%constant int REG__KEYPATH = 279;
%constant int REG__KEYRESULT = 1304;
%constant int REG__KEYRESULT_INTERNAL = 537;
%constant int REG__LASTWRITE = 1562;
%constant int REG__LINKCOUNT = 1307;
%constant int REG__LINKPATH = 284;
%constant int REG__LINKPATHSIZE = 1309;
%constant int REG__LINKTYPE = 1310;
%constant int REG__LOCK = 1311;
%constant int REG__NEWNAME = 288;
%constant int REG__NOTIFYFILTER = 1313;
%constant int REG__PATHBUFFER = 546;
%constant int REG__PERFORMANCEDATA = 547;
%constant int REG__REQLENGTH = 1316;
%constant int REG__RETURNSTATUS = 1317;
%constant int REG__SECACCESS = 1318;
%constant int REG__SECONDSTATUS = 1319;
%constant int REG__SECURITYPOLICY = 1320;
%constant int REG__SEGMENTNUMBER = 1321;
%constant int REG__SNAPSHOTDESTINATION = 1834;
%constant int REG__SNAPSHOTVERSIONS = 1323;
%constant int REG__SUBKEYINDEX = 1324;
%constant int REG__SUBKEYNAME = 301;
%constant int REG__SUBKEYNAMEMAX = 1326;
%constant int REG__SUBKEYNAMESIZE = 1327;
%constant int REG__SUBKEYSNUMBER = 1328;
%constant int REG__SECURITYINFORMATION = 1329;
%constant int REG__SECURITYDESCRIPTOR = 562;
%constant int REG__VALUEINDEX = 1331;
%constant int REG__VALUEDATA = 564;
%constant int REG__VALUEDATAMAX = 1333;
%constant int REG__VALUEDATASIZE = 1334;
%constant int REG__VALUENAME = 311;
%constant int REG__VALUENAMEMAX = 1336;
%constant int REG__VALUENAMESIZE = 1337;
%constant int REG__VALUENUMBER = 1338;
%constant int REG__VOLATILE = 1339;
%constant int REG__WILDASTERISK = 316;
%constant int REG__WILDPERCENT = 317;
%constant int REG__WILDPERIODS = 318;
%constant int REG__INSTRUMENTFILE = 575;
%constant int REG__INSTRUMENTKEY = 576;
%constant int REG__INSTRUMENTDATA = 577;
%constant int REG__FILENAME = 1858;
%constant int REG__COUNTER = 1347;
%constant int REG__SECDESCRIPTORLEN = 1348;
%constant int REG__SECDESCLEN_INTERNAL = 1349;
%constant int REG__VALUEDATASIZE_INTERNAL = 1350;
%constant int REG__SAMDESIRED = 1351;
%constant int REG__DATABASE_VERSION = 1352;
%constant int REG__LAST = 73;
%constant int REG_K_NONE = 0;
%constant int REG_K_CLUSTER = 1;
%constant int REG_K_SYSTEM = 2;
%constant int REG_K_PROCESS = 3;
%constant int REG_K_IMAGE = 4;
%constant int REG_K_WRITEBEHIND = 5;
%constant int REG_K_WRITETHRU = 6;
%constant int REG_K_CREATENEWKEY = 7;
%constant int REG_K_OPENEXISTINGKEY = 8;
%constant int REG_K_POLICY_OPENVMS = 9;
%constant int REG_K_POLICY_NT_40 = 10;
%constant int REG_K_INTERNAL = 11;
%constant int REG_K_HARDLINK = 12;
%constant int REG_K_SYMBOLICLINK = 13;
%constant int REG_K_BINARY = 14;
%constant int REG_K_DWORD = 15;
%constant int REG_K_DWLITTLEENDIAN = 16;
%constant int REG_K_DWBIGENDIAN = 17;
%constant int REG_K_EXPAND_SZ = 18;
%constant int REG_K_LINK = 19;
%constant int REG_K_MULTI_SZ = 20;
%constant int REG_K_QWORD = 21;
%constant int REG_K_RESOURCELIST = 22;
%constant int REG_K_SZ = 23;
%constant int REG_K_START_FILE = 24;
%constant int REG_K_START_PERF = 25;
%constant int REG_K_STOP_FILE = 26;
%constant int REG_K_STOP_PERF = 27;
%constant int REG_K_ZERO_FILE = 28;
%constant int REG_K_ZERO_PERF = 29;
%constant int REG_K_SHOW_CTR_FILE = 30;
%constant int REG_K_SHOW_CTR_PERF = 31;
%constant int REG_K_SHOW_FILE = 32;
%constant int REG_K_NORMAL = 33;
%constant int REG_K_LARGE = 34;
%constant int REG_K_EXACTMATCH = 35;
%constant int REG_K_INCLUDE = 36;
%constant int REG_K_EXCLUDE = 37;
%constant int REG_K_ANY = 38;
%constant int REG_K_NOTANY = 39;
%constant int REG_M_FC = 0x3FFL;
%constant int REG_M_CASE_SENSITIVE = 0x400L;
%constant int REG_M_DISABLE_WILDCARDS = 0x800L;
%constant int REG_M_IGNORE_LINKS = 0x1000L;
%constant int REG_M_NOW = 0x2000L;
%constant int REG_M_NOWAIT = 0x4000L;
%constant int REG_M_UNICODE_VALUES = 0x8000L;
%constant int REG_M_BYPASS = 0x10000L;
%constant int REG_M_INTERNAL = 0x20000L;
%constant int REG_S_REGDEF = 3;
%constant int REG_S_FC = 10;
%constant int REG_M_CHANGENAME = 0x1L;
%constant int REG_M_CHANGEATTRIBUTES = 0x2L;
%constant int REG_M_CHANGELASTSET = 0x4L;
%constant int REG_M_CHANGESECURITY = 0x8L;
%constant int REG_S_KEYCHANGEDEF = 1;
%constant int REG_M_ALLACCESS = 0x1L;
%constant int REG_M_CREATELINK = 0x2L;
%constant int REG_M_CREATESUBKEY = 0x4L;
%constant int REG_M_ENUMSUBKEYS = 0x8L;
%constant int REG_M_EXECUTE = 0x10L;
%constant int REG_M_NOTIFY = 0x20L;
%constant int REG_M_QUERYVALUE = 0x40L;
%constant int REG_M_READ = 0x80L;
%constant int REG_M_SETVALUE = 0x100L;
%constant int REG_M_WRITE = 0x200L;
%constant int REG_M_DELETEACCESS = 0x400L;
%constant int REG_M_READCONTROL = 0x800L;
%constant int REG_M_WRITEDAC = 0x1000L;
%constant int REG_M_WRITEOWNER = 0x2000L;
%constant int REG_M_SYNCHRONIZE = 0x4000L;
%constant int REG_M_ACCESSSYSTEMSECURITY = 0x8000L;
%constant int REG_M_MAXIMUMALLOWED = 0x10000L;
%constant int REG_M_GENERICALL = 0x20000L;
%constant int REG_M_GENERICEXECUTE = 0x40000L;
%constant int REG_M_GENERICWRITE = 0x80000L;
%constant int REG_M_GENERICREAD = 0x100000L;
%constant int REG_S_SECACCESSDEF = 3;
%constant int REG__HKEY_NONE = 0;
%constant int REG__HKEY_CLASSES_ROOT = -2147483648;
%constant int REG__HKEY_CURRENT_USER = -2147483647;
%constant int REG__HKEY_LOCAL_MACHINE = -2147483646;
%constant int REG__HKEY_USERS = -2147483645;
%constant int REG__HKEY_PERFORMANCE_DATA = -2147483644;
%constant int REG__HKEY_LAST_ROOT_KEY = 5;
