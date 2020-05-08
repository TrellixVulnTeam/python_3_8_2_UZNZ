%module rmsdef

%constant int RMS__FACILITY = 1;
%constant int RMS_V_STVSTATUS = 14;
%constant int RMS__SUC = 65537;
%constant int RMS__NORMAL = 65537;
%constant int RMS__STALL = 98305;
%constant int RMS__PENDING = 98313;
%constant int RMS__OK_DUP = 98321;
%constant int RMS__OK_IDX = 98329;
%constant int RMS__OK_RLK = 98337;
%constant int RMS__OK_RRL = 98345;
%constant int RMS__KFF = 98353;
%constant int RMS__OK_ALK = 98361;
%constant int RMS__OK_DEL = 98369;
%constant int RMS__OK_RNF = 98377;
%constant int RMS__OK_LIM = 98385;
%constant int RMS__OK_NOP = 98393;
%constant int RMS__OK_WAT = 98401;
%constant int RMS__CRE_STM = 98409;
%constant int RMS__OK_RULK = 98417;
%constant int RMS__SYNCH = 98425;
%constant int RMS__OK_ACT = 98433;
%constant int RMS__OK_NOCURTID = 98441;
%constant int RMS__CONTROLC = 67153;
%constant int RMS__CONTROLO = 67081;
%constant int RMS__CONTROLY = 67089;
%constant int RMS__CREATED = 67097;
%constant int RMS__SUPERSEDE = 67121;
%constant int RMS__OVRDSKQUOTA = 67177;
%constant int RMS__FILEPURGED = 67193;
%constant int RMS__BOF = 98712;
%constant int RMS__RNL = 98720;
%constant int RMS__RTB = 98728;
%constant int RMS__TMO = 98736;
%constant int RMS__TNS = 98744;
%constant int RMS__BES = 98752;
%constant int RMS__PES = 98760;
%constant int RMS__ACT = 98906;
%constant int RMS__DEL = 98914;
%constant int RMS__INCOMPSHR = 98922;
%constant int RMS__DNR = 98930;
%constant int RMS__EOF = 98938;
%constant int RMS__FEX = 98946;
%constant int RMS__FLK = 98954;
%constant int RMS__FNF = 98962;
%constant int RMS__PRV = 98970;
%constant int RMS__REX = 98978;
%constant int RMS__RLK = 98986;
%constant int RMS__RNF = 98994;
%constant int RMS__WLK = 99002;
%constant int RMS__EXP = 99010;
%constant int RMS__NMF = 99018;
%constant int RMS__SUP = 99026;
%constant int RMS__RSA = 99034;
%constant int RMS__CRC = 99042;
%constant int RMS__WCC = 99050;
%constant int RMS__IDR = 99058;
%constant int RMS__LWC = 99066;
%constant int RMS__UNUSED1 = 99074;
%constant int RMS__NOVALPRS = 99082;
%constant int RMS__KEY_MISMATCH = 99090;
%constant int RMS__RUH = 99098;
%constant int RMS__JND = 99106;
%constant int RMS__BADPHASE = 99114;
%constant int RMS__TOWDR = 99122;
%constant int RMS__NEXDR = 99130;
%constant int RMS__INVDRMSG = 99138;
%constant int RMS__RU_ACTIVE = 99146;
%constant int RMS__UNKRUFAC = 99154;
%constant int RMS__LIMBO = 99162;
%constant int RMS__IVATRACE = 99170;
%constant int RMS__OPNOTSUP = 99178;
%constant int RMS__EXTNOTFOU = 99186;
%constant int RMS__EXT_ERR = 99194;
%constant int RMS__SEMANTICS = 99202;
%constant int RMS__LSCAN = 99210;
%constant int RMS__ROOTSRCH = 99218;
%constant int RMS__IDXSEARCH = 99226;
%constant int RMS__NETBTS = 99234;
%constant int RMS__NXR = 99242;
%constant int RMS__EOFASY_SYNCH = 99250;
%constant int RMS__ELOOP = 99258;
%constant int RMS__ACC = 114690;
%constant int RMS__CRE = 114698;
%constant int RMS__DAC = 114706;
%constant int RMS__ENT = 114714;
%constant int RMS__EXT = 114722;
%constant int RMS__FND = 114730;
%constant int RMS__MKD = 114738;
%constant int RMS__DPE = 114746;
%constant int RMS__SPL = 114754;
%constant int RMS__DNF = 114762;
%constant int RMS__RUF = 114770;
%constant int RMS__WRTJNL_AIJ = 114778;
%constant int RMS__WRTJNL_BIJ = 114786;
%constant int RMS__WRTJNL_ATJ = 114794;
%constant int RMS__WRTJNL_RUJ = 114802;
%constant int RMS__RRF = 114810;
%constant int RMS__DDTM_ERR = 114818;
%constant int RMS__DTFCDDREC = 99308;
%constant int RMS__AID = 99316;
%constant int RMS__ALN = 99324;
%constant int RMS__ALQ = 99332;
%constant int RMS__ANI = 99340;
%constant int RMS__AOP = 99348;
%constant int RMS__BKS = 99356;
%constant int RMS__BKZ = 99364;
%constant int RMS__BLN = 99372;
%constant int RMS__BUG = 99380;
%constant int RMS__BUG_DDI = 99388;
%constant int RMS__BUG_DAP = 99396;
%constant int RMS__BUG_RU_ACTIVE = 99404;
%constant int RMS__BUG_RURECERR = 99412;
%constant int RMS__BUG_FLUSH_JNL_FAILED = 99420;
%constant int RMS__BUG_RU_ABORT_FAIL = 99428;
%constant int RMS__BUG_RU_COMMIT_FAIL = 99436;
%constant int RMS__BUG_XX6 = 99444;
%constant int RMS__BUG_XX7 = 99452;
%constant int RMS__BUG_XX8 = 99460;
%constant int RMS__BUSY = 99468;
%constant int RMS__CCR = 99476;
%constant int RMS__CHG = 99484;
%constant int RMS__CHK = 99492;
%constant int RMS__COD = 99500;
%constant int RMS__CUR = 99508;
%constant int RMS__DAN = 99516;
%constant int RMS__DEV = 99524;
%constant int RMS__DIR = 99532;
%constant int RMS__DME = 99540;
%constant int RMS__DNA = 99548;
%constant int RMS__DTP = 99556;
%constant int RMS__DUP = 99564;
%constant int RMS__DVI = 99572;
%constant int RMS__ESA = 99580;
%constant int RMS__ESS = 99588;
%constant int RMS__FAB = 99596;
%constant int RMS__FAC = 99604;
%constant int RMS__FLG = 99612;
%constant int RMS__FNA = 99620;
%constant int RMS__FNM = 99628;
%constant int RMS__FSZ = 99636;
%constant int RMS__FOP = 99644;
%constant int RMS__FUL = 99652;
%constant int RMS__IAL = 99660;
%constant int RMS__IAN = 99668;
%constant int RMS__IDX = 99676;
%constant int RMS__IFI = 99684;
%constant int RMS__IMX = 99692;
%constant int RMS__IOP = 99700;
%constant int RMS__IRC = 99708;
%constant int RMS__ISI = 99716;
%constant int RMS__KBF = 99724;
%constant int RMS__KEY = 99732;
%constant int RMS__KRF = 99740;
%constant int RMS__KSZ = 99748;
%constant int RMS__LAN = 99756;
%constant int RMS__RUNDOWN = 99764;
%constant int RMS__LNE = 99772;
%constant int RMS__DTFCVT = 99780;
%constant int RMS__MRN = 99788;
%constant int RMS__MRS = 99796;
%constant int RMS__NAM = 99804;
%constant int RMS__NEF = 99812;
%constant int RMS__DTFQUASYN = 99820;
%constant int RMS__NOD = 99828;
%constant int RMS__NPK = 99836;
%constant int RMS__ORD = 99844;
%constant int RMS__ORG = 99852;
%constant int RMS__PBF = 99860;
%constant int RMS__PLG = 99868;
%constant int RMS__POS = 99876;
%constant int RMS__DTFQUAVAL = 99884;
%constant int RMS__QUO = 99892;
%constant int RMS__RAB = 99900;
%constant int RMS__RAC = 99908;
%constant int RMS__RAT = 99916;
%constant int RMS__RBF = 99924;
%constant int RMS__RFA = 99932;
%constant int RMS__RFM = 99940;
%constant int RMS__RHB = 99948;
%constant int RMS__RLF = 99956;
%constant int RMS__ROP = 99964;
%constant int RMS__RRV = 99972;
%constant int RMS__RVU = 99980;
%constant int RMS__RSS = 99988;
%constant int RMS__RST = 99996;
%constant int RMS__RSZ = 100004;
%constant int RMS__SEQ = 100012;
%constant int RMS__SHR = 100020;
%constant int RMS__SIZ = 100028;
%constant int RMS__SQO = 100036;
%constant int RMS__DTFSESEST = 100044;
%constant int RMS__SYN = 100052;
%constant int RMS__TRE = 100060;
%constant int RMS__TYP = 100068;
%constant int RMS__UBF = 100076;
%constant int RMS__USZ = 100084;
%constant int RMS__VER = 100092;
%constant int RMS__XNF = 100100;
%constant int RMS__XAB = 100108;
%constant int RMS__ESL = 100116;
%constant int RMS__DTFSESTER = 100124;
%constant int RMS__ENV = 100132;
%constant int RMS__PLV = 100140;
%constant int RMS__MBC = 100148;
%constant int RMS__RSL = 100156;
%constant int RMS__WLD = 100164;
%constant int RMS__NET = 100172;
%constant int RMS__IBF = 100180;
%constant int RMS__REF = 100188;
%constant int RMS__IFL = 100196;
%constant int RMS__DFL = 100204;
%constant int RMS__KNM = 100212;
%constant int RMS__IBK = 100220;
%constant int RMS__KSI = 100228;
%constant int RMS__LEX = 100236;
%constant int RMS__SEG = 100244;
%constant int RMS__SNE = 100252;
%constant int RMS__SPE = 100260;
%constant int RMS__UPI = 100268;
%constant int RMS__ACS = 100276;
%constant int RMS__STR = 100284;
%constant int RMS__FTM = 100292;
%constant int RMS__GBC = 100300;
%constant int RMS__DEADLOCK = 100308;
%constant int RMS__EXENQLM = 100316;
%constant int RMS__JOP = 100324;
%constant int RMS__RUM = 100332;
%constant int RMS__JNS = 100340;
%constant int RMS__NRU = 100348;
%constant int RMS__IFF = 100356;
%constant int RMS__DTFTRATBL = 100364;
%constant int RMS__DTFUNSTYP = 100372;
%constant int RMS__DTFVERMIS = 100380;
%constant int RMS__DTFACC = 100386;
%constant int RMS__BOGUSCOL = 100396;
%constant int RMS__ERRREADCOL = 100404;
%constant int RMS__ERRWRITECOL = 100412;
%constant int RMS__SNS = 100420;
%constant int RMS__NOEXTEND = 100428;
%constant int RMS__DTFCRE = 100434;
%constant int RMS__DELJNS = 100444;
%constant int RMS__NOTSAMEJNL = 100452;
%constant int RMS__SNPPF = 100460;
%constant int RMS__NAML = 100468;
%constant int RMS__NAMLESS = 100476;
%constant int RMS__NAMLRSS = 100484;
%constant int RMS__NAMLFSSIZ = 100492;
%constant int RMS__NAMLFSINV = 100500;
%constant int RMS__BADGBH = 100508;
%constant int RMS__BADGBD = 100516;
%constant int RMS__FOPEXTMBZ = 100524;
%constant int RMS__INVOP_SSIO = 100532;
%constant int RMS__IVSF = 100540;
%constant int RMS__ATR = 114892;
%constant int RMS__ATW = 114900;
%constant int RMS__CCF = 114908;
%constant int RMS__CDA = 114916;
%constant int RMS__CHN = 114924;
%constant int RMS__RER = 114932;
%constant int RMS__RMV = 114940;
%constant int RMS__RPL = 114948;
%constant int RMS__SYS = 114956;
%constant int RMS__WER = 114964;
%constant int RMS__WPL = 114972;
%constant int RMS__IFA = 114980;
%constant int RMS__WBE = 114988;
%constant int RMS__ENQ = 114996;
%constant int RMS__NETFAIL = 115004;
%constant int RMS__SUPPORT = 115012;
%constant int RMS__CRMP = 115020;
%constant int RMS__DTFCFGFIL = 115028;
%constant int RMS__REENT = 115036;
%constant int RMS__ACC_RUJ = 115044;
%constant int RMS__TMR = 115052;
%constant int RMS__ACC_AIJ = 115060;
%constant int RMS__ACC_BIJ = 115068;
%constant int RMS__ACC_ATJ = 115076;
%constant int RMS__DTFDEFFIL = 115084;
%constant int RMS__DTFREGFIL = 115092;
%constant int RMS__JNLNOTAUTH = 115100;
%constant int RMS__CRBUFOBJ = 115108;
%constant int RMS__RSESTK_ALLOC = 115116;