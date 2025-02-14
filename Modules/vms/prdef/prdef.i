%module prdef

%constant int PR__ESP = 1;
%constant int PR__SSP = 2;
%constant int PR__USP = 3;
%constant int PR__ASN = 6;
%constant int PR__ASTEN = 48;
%constant int PR__ASTSR = 49;
%constant int PR__DATFX = 23;
%constant int PR__IPIR = 22;
%constant int PR__IPL = 18;
%constant int PR__MCES = 38;
%constant int PR__PCBB = 16;
%constant int PR__PME = 61;
%constant int PR__PRBR = 15;
%constant int PR__SCBB = 17;
%constant int PR__SIRR = 20;
%constant int PR__SISR = 21;
%constant int PR__TBIA = 57;
%constant int PR__TBIAP = 50;
%constant int PR__TBIS = 58;
%constant int PR__TBIS_64 = 60;
%constant int PR__TBISD = 59;
%constant int PR__TBISI = 47;
%constant int PR__VPTB = 12;
%constant int PR__SID_TYP780 = 1;
%constant int PR__SID_TYP750 = 2;
%constant int PR__SID_TYP730 = 3;
%constant int PR__SID_TYP790 = 4;
%constant int PR__SID_TYP8SS = 5;
%constant int PR__SID_TYP8NN = 6;
%constant int PR__SID_TYPUV1 = 7;
%constant int PR__SID_TYPUV2 = 8;
%constant int PR__SID_TYP410 = 8;
%constant int PR__SID_TYP009 = 9;
%constant int PR__SID_TYP420 = 10;
%constant int PR__SID_TYP520 = 10;
%constant int PR__SID_TYP650 = 10;
%constant int PR__SID_TYP9CC = 10;
%constant int PR__SID_TYP9CI = 10;
%constant int PR__SID_TYP60 = 10;
%constant int PR__SID_TYP670 = 11;
%constant int PR__SID_TYP9RR = 11;
%constant int PR__SID_TYP43 = 11;
%constant int PR__SID_TYP9AQ = 14;
%constant int PR__SID_TYP8PS = 17;
%constant int PR__SID_TYP1202 = 18;
%constant int PR__SID_TYP46 = 18;
%constant int PR__SID_TYP600 = 19;
%constant int PR__SID_TYP690 = 19;
%constant int PR__SID_TYP700 = 19;
%constant int PR__SID_TYP1302 = 19;
%constant int PR__SID_TYP49 = 19;
%constant int PR__SID_TYP1303 = 19;
%constant int PR__SID_TYP660 = 20;
%constant int PR__SID_TYP440 = 20;
%constant int PR__SID_TYP4A = 20;
%constant int PR__SID_TYP550 = 20;
%constant int PR__SID_TYP1701 = 23;
%constant int PR__SID_TYPMAX = 23;
%constant int PR__SID_TYP_NOTAVAX = 128;
%constant int PR__SID_TYPUV = 8;
%constant int PR__XSID_UV_UV = 0;
%constant int PR__XSID_UV_UV2 = 1;
%constant int PR__XSID_UV_410 = 4;
%constant int PR__SID_TYPCV = 10;
%constant int PR__XSID_CV_CV = 0;
%constant int PR__XSID_CV_650 = 1;
%constant int PR__XSID_CV_9CC = 2;
%constant int PR__XSID_CV_60 = 3;
%constant int PR__XSID_CV_420 = 4;
%constant int PR__XSID_CV_9CI = 5;
%constant int PR__XSID_CV_520 = 7;
%constant int PR__SID_TYPRV = 11;
%constant int PR__XSID_RV_RV = 0;
%constant int PR__XSID_RV_670 = 1;
%constant int PR__XSID_RV_9RR = 2;
%constant int PR__XSID_RV_43 = 4;
%constant int PR__SID_TYPV12 = 18;
%constant int PR__XSID_V12_V12 = 0;
%constant int PR__XSID_V12_1202 = 2;
%constant int PR__XSID_V12_46 = 4;
%constant int PR__SID_TYPV13 = 19;
%constant int PR__XSID_V13_V13 = 0;
%constant int PR__XSID_V13_690 = 1;
%constant int PR__XSID_V13_1302 = 2;
%constant int PR__XSID_V13_1303 = 3;
%constant int PR__XSID_V13_49 = 4;
%constant int PR__XSID_V13_700 = 5;
%constant int PR__XSID_V13_600 = 6;
%constant int PR__SID_TYPV14 = 20;
%constant int PR__XSID_V14_V14 = 0;
%constant int PR__XSID_V14_660 = 1;
%constant int PR__XSID_V14_440 = 4;
%constant int PR__XSID_V14_4A = 5;
%constant int PR__XSID_V14_550 = 7;
%constant int PR__SID_TYPV17 = 23;
%constant int PR__XSID_V17_V17 = 0;
%constant int PR__XSID_V17_1701 = 1;
%constant int PR__XSID_N8800 = 0;
%constant int PR__XSID_N8700 = 1;
%constant int PR__XSID_N2 = 2;
%constant int PR__XSID_N3 = 3;
%constant int PR__XSID_N4 = 4;
%constant int PR__XSID_N5 = 5;
%constant int PR__XSID_N8550 = 6;
%constant int PR__XSID_N8500 = 7;
%constant int PR__XSID_N8NNN = -1;
%constant int PR_M_ASTEN = 0xFL;
%constant int PR_M_ASTEN_KEN = 0x1L;
%constant int PR_M_ASTEN_EEN = 0x2L;
%constant int PR_M_ASTEN_SEN = 0x4L;
%constant int PR_M_ASTEN_UEN = 0x8L;
%constant int PR_M_ASTEN_DSBL_ALL = 0;
%constant int PR_M_ASTEN_ENBL_ALL = 255;
%constant int PR_M_ASTEN_ENBL_K = 17;
%constant int PR_M_ASTEN_ENBL_E = 34;
%constant int PR_M_ASTEN_ENBL_S = 68;
%constant int PR_M_ASTEN_ENBL_U = 136;
%constant int PR_M_ASTEN_PRSRV_ALL = 15;
%constant int PR_M_ASTEN_PRSRV_K = 1;
%constant int PR_M_ASTEN_PRSRV_E = 2;
%constant int PR_M_ASTEN_PRSRV_S = 4;
%constant int PR_M_ASTEN_PRSRV_U = 8;
%constant int PR_M_ASTSR = 0xFL;
%constant int PR_M_ASTSR_KPD = 0x1L;
%constant int PR_M_ASTSR_EPD = 0x2L;
%constant int PR_M_ASTSR_SPD = 0x4L;
%constant int PR_M_ASTSR_UPD = 0x8L;
%constant int PR_M_ASTSR_CLR_ALL = 0;
%constant int PR_M_ASTSR_SET_ALL = 255;
%constant int PR_M_ASTSR_SET_K = 17;
%constant int PR_M_ASTSR_SET_E = 34;
%constant int PR_M_ASTSR_SET_S = 68;
%constant int PR_M_ASTSR_SET_U = 136;
%constant int PR_M_ASTSR_PRSRV_ALL = 15;
%constant int PR_M_ASTSR_PRSRV_K = 1;
%constant int PR_M_ASTSR_PRSRV_E = 2;
%constant int PR_M_ASTSR_PRSRV_S = 4;
%constant int PR_M_ASTSR_PRSRV_U = 8;
%constant int PR_M_FEN_FEN = 0x1L;
%constant int PR_M_DATFX_DATFX = 0x1L;
%constant int PR_M_IPL_IPL = 0x1FL;
%constant int PR_M_MCES_MCK = 0x1L;
%constant int PR_M_MCES_SCE = 0x2L;
%constant int PR_M_MCES_PCE = 0x4L;
%constant int PR_M_MCES_DPC = 0x8L;
%constant int PR_M_MCES_DSC = 0x10L;
%constant int PR_V_PCBB_PA = 0;
%constant int PR_S_PCBB_PA = 48;
%constant int PR_M_PS_SW = 0x3L;
%constant int PR_M_PS_PRVMOD = 0x3L;
%constant int PR_M_PS_SYSSTATE = 0x4L;
%constant int PR_M_PS_CURMOD = 0x18L;
%constant int PR_M_PS_VMM = 0x80L;
%constant int PR_M_PS_IPL = 0x1F00L;
%constant int PR_M_PS_SP_ALIGN = 0x3F00000000000000L;
%constant int PR_M_PS_MBZ_62 = 0x4000000000000000L;
%constant int PR_M_PS_MBZ_63 = 0x8000000000000000L;
%constant int PR_V_PS_MAX_PS_REG_BIT = 13;
%constant int PR_C_PS_KERNEL = 0;
%constant int PR_C_PS_EXEC = 1;
%constant int PR_C_PS_SUPER = 2;
%constant int PR_C_PS_USER = 3;
%constant int PR_M_PTBR_PFN = 0xFFFFFFFFL;
%constant int PR_M_SCBB_PFN = 0xFFFFFFFFL;
%constant int PR_M_SIRR_LVL = 0xFL;
%constant int PR_M_SISR_SUMMARY = 0xFFFFL;
%constant int PR_M_SISR_RAZ = 0x1L;
%constant int PR_M_SISR_IR1 = 0x2L;
%constant int PR_M_SISR_IR2 = 0x4L;
%constant int PR_M_SISR_IR3 = 0x8L;
%constant int PR_M_SISR_IR4 = 0x10L;
%constant int PR_M_SISR_IR5 = 0x20L;
%constant int PR_M_SISR_IR6 = 0x40L;
%constant int PR_M_SISR_IR7 = 0x80L;
%constant int PR_M_SISR_IR8 = 0x100L;
%constant int PR_M_SISR_IR9 = 0x200L;
%constant int PR_M_SISR_IR10 = 0x400L;
%constant int PR_M_SISR_IR11 = 0x800L;
%constant int PR_M_SISR_IR12 = 0x1000L;
%constant int PR_M_SISR_IR13 = 0x2000L;
%constant int PR_M_SISR_IR14 = 0x4000L;
%constant int PR_M_SISR_IR15 = 0x8000L;
%constant int PR_M_TBCHK_VA_PRESENT = 0x1L;
%constant int PR_M_IEEE_DNOD = 0x800000000000L;
%constant int PR_M_IEEE_DNZ = 0x1000000000000L;
%constant int PR_M_IEEE_INVD = 0x2000000000000L;
%constant int PR_M_IEEE_DZED = 0x4000000000000L;
%constant int PR_M_IEEE_OVFD = 0x8000000000000L;
%constant int PR_M_IEEE_INV = 0x10000000000000L;
%constant int PR_M_IEEE_DZE = 0x20000000000000L;
%constant int PR_M_IEEE_OVF = 0x40000000000000L;
%constant int PR_M_IEEE_UNF = 0x80000000000000L;
%constant int PR_M_IEEE_INE = 0x100000000000000L;
%constant int PR_M_IEEE_IOV = 0x200000000000000L;
%constant int PR_M_IEEE_UNDZ = 0x1000000000000000L;
%constant int PR_M_IEEE_UNFD = 0x2000000000000000L;
%constant int PR_M_IEEE_INED = 0x4000000000000000L;
%constant int PR_M_IEEE_SUMMARY = 0x8000000000000000L;
%constant int PR_S_PRDEF = 8;
%constant int PR_S_QUAD_ACCESS = 8;
%constant int PR_S_LONG_ACCESS = 8;
%constant int PR_S_SID_SN = 12;
%constant int PR_S_SID_PL = 3;
%constant int PR_S_SID_ECO = 9;
%constant int PR_S_SID_TYPE = 8;
%constant int PR_S_XSID_TYPE = 8;
%constant int PR_S_ASTEN = 4;
%constant int PR_S_ASTSR = 4;
%constant int PR_S_IPL_IPL = 5;
%constant int PR_S_PS_SW = 2;
%constant int PR_S_PS_PRVMOD = 2;
%constant int PR_S_PS_CURMOD = 2;
%constant int PR_S_PS_IPL = 5;
%constant int PR_S_PS_SP_ALIGN = 6;
%constant int PR_S_PTBR_PFN = 32;
%constant int PR_S_SCBB_PFN = 32;
%constant int PR_S_SIRR_LVL = 4;
%constant int PR_S_SISR_SUMMARY = 16;
%constant int PR_S_IEEE_DYN_RND = 2;
