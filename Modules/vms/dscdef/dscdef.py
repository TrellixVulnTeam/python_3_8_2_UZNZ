# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_dscdef', [dirname(__file__)])
        except ImportError:
            import _dscdef
            return _dscdef
        if fp is not None:
            try:
                _mod = imp.load_module('_dscdef', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _dscdef = swig_import_helper()
    del swig_import_helper
else:
    import _dscdef
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_dscdef.DSC_K_DTYPE_Z_swigconstant(_dscdef)
DSC_K_DTYPE_Z = _dscdef.DSC_K_DTYPE_Z

_dscdef.DSC64_K_DTYPE_Z_swigconstant(_dscdef)
DSC64_K_DTYPE_Z = _dscdef.DSC64_K_DTYPE_Z

_dscdef.DSC_K_DTYPE_BU_swigconstant(_dscdef)
DSC_K_DTYPE_BU = _dscdef.DSC_K_DTYPE_BU

_dscdef.DSC64_K_DTYPE_BU_swigconstant(_dscdef)
DSC64_K_DTYPE_BU = _dscdef.DSC64_K_DTYPE_BU

_dscdef.DSC_K_DTYPE_WU_swigconstant(_dscdef)
DSC_K_DTYPE_WU = _dscdef.DSC_K_DTYPE_WU

_dscdef.DSC64_K_DTYPE_WU_swigconstant(_dscdef)
DSC64_K_DTYPE_WU = _dscdef.DSC64_K_DTYPE_WU

_dscdef.DSC_K_DTYPE_LU_swigconstant(_dscdef)
DSC_K_DTYPE_LU = _dscdef.DSC_K_DTYPE_LU

_dscdef.DSC64_K_DTYPE_LU_swigconstant(_dscdef)
DSC64_K_DTYPE_LU = _dscdef.DSC64_K_DTYPE_LU

_dscdef.DSC_K_DTYPE_QU_swigconstant(_dscdef)
DSC_K_DTYPE_QU = _dscdef.DSC_K_DTYPE_QU

_dscdef.DSC64_K_DTYPE_QU_swigconstant(_dscdef)
DSC64_K_DTYPE_QU = _dscdef.DSC64_K_DTYPE_QU

_dscdef.DSC_K_DTYPE_OU_swigconstant(_dscdef)
DSC_K_DTYPE_OU = _dscdef.DSC_K_DTYPE_OU

_dscdef.DSC64_K_DTYPE_OU_swigconstant(_dscdef)
DSC64_K_DTYPE_OU = _dscdef.DSC64_K_DTYPE_OU

_dscdef.DSC_K_DTYPE_B_swigconstant(_dscdef)
DSC_K_DTYPE_B = _dscdef.DSC_K_DTYPE_B

_dscdef.DSC64_K_DTYPE_B_swigconstant(_dscdef)
DSC64_K_DTYPE_B = _dscdef.DSC64_K_DTYPE_B

_dscdef.DSC_K_DTYPE_W_swigconstant(_dscdef)
DSC_K_DTYPE_W = _dscdef.DSC_K_DTYPE_W

_dscdef.DSC64_K_DTYPE_W_swigconstant(_dscdef)
DSC64_K_DTYPE_W = _dscdef.DSC64_K_DTYPE_W

_dscdef.DSC_K_DTYPE_L_swigconstant(_dscdef)
DSC_K_DTYPE_L = _dscdef.DSC_K_DTYPE_L

_dscdef.DSC64_K_DTYPE_L_swigconstant(_dscdef)
DSC64_K_DTYPE_L = _dscdef.DSC64_K_DTYPE_L

_dscdef.DSC_K_DTYPE_Q_swigconstant(_dscdef)
DSC_K_DTYPE_Q = _dscdef.DSC_K_DTYPE_Q

_dscdef.DSC64_K_DTYPE_Q_swigconstant(_dscdef)
DSC64_K_DTYPE_Q = _dscdef.DSC64_K_DTYPE_Q

_dscdef.DSC_K_DTYPE_O_swigconstant(_dscdef)
DSC_K_DTYPE_O = _dscdef.DSC_K_DTYPE_O

_dscdef.DSC64_K_DTYPE_O_swigconstant(_dscdef)
DSC64_K_DTYPE_O = _dscdef.DSC64_K_DTYPE_O

_dscdef.DSC_K_DTYPE_F_swigconstant(_dscdef)
DSC_K_DTYPE_F = _dscdef.DSC_K_DTYPE_F

_dscdef.DSC64_K_DTYPE_F_swigconstant(_dscdef)
DSC64_K_DTYPE_F = _dscdef.DSC64_K_DTYPE_F

_dscdef.DSC_K_DTYPE_D_swigconstant(_dscdef)
DSC_K_DTYPE_D = _dscdef.DSC_K_DTYPE_D

_dscdef.DSC64_K_DTYPE_D_swigconstant(_dscdef)
DSC64_K_DTYPE_D = _dscdef.DSC64_K_DTYPE_D

_dscdef.DSC_K_DTYPE_G_swigconstant(_dscdef)
DSC_K_DTYPE_G = _dscdef.DSC_K_DTYPE_G

_dscdef.DSC64_K_DTYPE_G_swigconstant(_dscdef)
DSC64_K_DTYPE_G = _dscdef.DSC64_K_DTYPE_G

_dscdef.DSC_K_DTYPE_H_swigconstant(_dscdef)
DSC_K_DTYPE_H = _dscdef.DSC_K_DTYPE_H

_dscdef.DSC64_K_DTYPE_H_swigconstant(_dscdef)
DSC64_K_DTYPE_H = _dscdef.DSC64_K_DTYPE_H

_dscdef.DSC_K_DTYPE_FC_swigconstant(_dscdef)
DSC_K_DTYPE_FC = _dscdef.DSC_K_DTYPE_FC

_dscdef.DSC64_K_DTYPE_FC_swigconstant(_dscdef)
DSC64_K_DTYPE_FC = _dscdef.DSC64_K_DTYPE_FC

_dscdef.DSC_K_DTYPE_DC_swigconstant(_dscdef)
DSC_K_DTYPE_DC = _dscdef.DSC_K_DTYPE_DC

_dscdef.DSC64_K_DTYPE_DC_swigconstant(_dscdef)
DSC64_K_DTYPE_DC = _dscdef.DSC64_K_DTYPE_DC

_dscdef.DSC_K_DTYPE_GC_swigconstant(_dscdef)
DSC_K_DTYPE_GC = _dscdef.DSC_K_DTYPE_GC

_dscdef.DSC64_K_DTYPE_GC_swigconstant(_dscdef)
DSC64_K_DTYPE_GC = _dscdef.DSC64_K_DTYPE_GC

_dscdef.DSC_K_DTYPE_HC_swigconstant(_dscdef)
DSC_K_DTYPE_HC = _dscdef.DSC_K_DTYPE_HC

_dscdef.DSC64_K_DTYPE_HC_swigconstant(_dscdef)
DSC64_K_DTYPE_HC = _dscdef.DSC64_K_DTYPE_HC

_dscdef.DSC_K_DTYPE_FS_swigconstant(_dscdef)
DSC_K_DTYPE_FS = _dscdef.DSC_K_DTYPE_FS

_dscdef.DSC64_K_DTYPE_FS_swigconstant(_dscdef)
DSC64_K_DTYPE_FS = _dscdef.DSC64_K_DTYPE_FS

_dscdef.DSC_K_DTYPE_FT_swigconstant(_dscdef)
DSC_K_DTYPE_FT = _dscdef.DSC_K_DTYPE_FT

_dscdef.DSC64_K_DTYPE_FT_swigconstant(_dscdef)
DSC64_K_DTYPE_FT = _dscdef.DSC64_K_DTYPE_FT

_dscdef.DSC_K_DTYPE_FSC_swigconstant(_dscdef)
DSC_K_DTYPE_FSC = _dscdef.DSC_K_DTYPE_FSC

_dscdef.DSC64_K_DTYPE_FSC_swigconstant(_dscdef)
DSC64_K_DTYPE_FSC = _dscdef.DSC64_K_DTYPE_FSC

_dscdef.DSC_K_DTYPE_FTC_swigconstant(_dscdef)
DSC_K_DTYPE_FTC = _dscdef.DSC_K_DTYPE_FTC

_dscdef.DSC64_K_DTYPE_FTC_swigconstant(_dscdef)
DSC64_K_DTYPE_FTC = _dscdef.DSC64_K_DTYPE_FTC

_dscdef.DSC_K_DTYPE_FX_swigconstant(_dscdef)
DSC_K_DTYPE_FX = _dscdef.DSC_K_DTYPE_FX

_dscdef.DSC64_K_DTYPE_FX_swigconstant(_dscdef)
DSC64_K_DTYPE_FX = _dscdef.DSC64_K_DTYPE_FX

_dscdef.DSC_K_DTYPE_FXC_swigconstant(_dscdef)
DSC_K_DTYPE_FXC = _dscdef.DSC_K_DTYPE_FXC

_dscdef.DSC64_K_DTYPE_FXC_swigconstant(_dscdef)
DSC64_K_DTYPE_FXC = _dscdef.DSC64_K_DTYPE_FXC

_dscdef.DSC_K_DTYPE_CIT_swigconstant(_dscdef)
DSC_K_DTYPE_CIT = _dscdef.DSC_K_DTYPE_CIT

_dscdef.DSC64_K_DTYPE_CIT_swigconstant(_dscdef)
DSC64_K_DTYPE_CIT = _dscdef.DSC64_K_DTYPE_CIT

_dscdef.DSC_K_DTYPE_T_swigconstant(_dscdef)
DSC_K_DTYPE_T = _dscdef.DSC_K_DTYPE_T

_dscdef.DSC64_K_DTYPE_T_swigconstant(_dscdef)
DSC64_K_DTYPE_T = _dscdef.DSC64_K_DTYPE_T

_dscdef.DSC_K_DTYPE_VT_swigconstant(_dscdef)
DSC_K_DTYPE_VT = _dscdef.DSC_K_DTYPE_VT

_dscdef.DSC64_K_DTYPE_VT_swigconstant(_dscdef)
DSC64_K_DTYPE_VT = _dscdef.DSC64_K_DTYPE_VT

_dscdef.DSC_K_DTYPE_T2_swigconstant(_dscdef)
DSC_K_DTYPE_T2 = _dscdef.DSC_K_DTYPE_T2

_dscdef.DSC64_K_DTYPE_T2_swigconstant(_dscdef)
DSC64_K_DTYPE_T2 = _dscdef.DSC64_K_DTYPE_T2

_dscdef.DSC_K_DTYPE_NU_swigconstant(_dscdef)
DSC_K_DTYPE_NU = _dscdef.DSC_K_DTYPE_NU

_dscdef.DSC64_K_DTYPE_NU_swigconstant(_dscdef)
DSC64_K_DTYPE_NU = _dscdef.DSC64_K_DTYPE_NU

_dscdef.DSC_K_DTYPE_NL_swigconstant(_dscdef)
DSC_K_DTYPE_NL = _dscdef.DSC_K_DTYPE_NL

_dscdef.DSC64_K_DTYPE_NL_swigconstant(_dscdef)
DSC64_K_DTYPE_NL = _dscdef.DSC64_K_DTYPE_NL

_dscdef.DSC_K_DTYPE_NLO_swigconstant(_dscdef)
DSC_K_DTYPE_NLO = _dscdef.DSC_K_DTYPE_NLO

_dscdef.DSC64_K_DTYPE_NLO_swigconstant(_dscdef)
DSC64_K_DTYPE_NLO = _dscdef.DSC64_K_DTYPE_NLO

_dscdef.DSC_K_DTYPE_NR_swigconstant(_dscdef)
DSC_K_DTYPE_NR = _dscdef.DSC_K_DTYPE_NR

_dscdef.DSC64_K_DTYPE_NR_swigconstant(_dscdef)
DSC64_K_DTYPE_NR = _dscdef.DSC64_K_DTYPE_NR

_dscdef.DSC_K_DTYPE_NRO_swigconstant(_dscdef)
DSC_K_DTYPE_NRO = _dscdef.DSC_K_DTYPE_NRO

_dscdef.DSC64_K_DTYPE_NRO_swigconstant(_dscdef)
DSC64_K_DTYPE_NRO = _dscdef.DSC64_K_DTYPE_NRO

_dscdef.DSC_K_DTYPE_NZ_swigconstant(_dscdef)
DSC_K_DTYPE_NZ = _dscdef.DSC_K_DTYPE_NZ

_dscdef.DSC64_K_DTYPE_NZ_swigconstant(_dscdef)
DSC64_K_DTYPE_NZ = _dscdef.DSC64_K_DTYPE_NZ

_dscdef.DSC_K_DTYPE_P_swigconstant(_dscdef)
DSC_K_DTYPE_P = _dscdef.DSC_K_DTYPE_P

_dscdef.DSC64_K_DTYPE_P_swigconstant(_dscdef)
DSC64_K_DTYPE_P = _dscdef.DSC64_K_DTYPE_P

_dscdef.DSC_K_DTYPE_V_swigconstant(_dscdef)
DSC_K_DTYPE_V = _dscdef.DSC_K_DTYPE_V

_dscdef.DSC64_K_DTYPE_V_swigconstant(_dscdef)
DSC64_K_DTYPE_V = _dscdef.DSC64_K_DTYPE_V

_dscdef.DSC_K_DTYPE_VU_swigconstant(_dscdef)
DSC_K_DTYPE_VU = _dscdef.DSC_K_DTYPE_VU

_dscdef.DSC64_K_DTYPE_VU_swigconstant(_dscdef)
DSC64_K_DTYPE_VU = _dscdef.DSC64_K_DTYPE_VU

_dscdef.DSC_K_DTYPE_ZI_swigconstant(_dscdef)
DSC_K_DTYPE_ZI = _dscdef.DSC_K_DTYPE_ZI

_dscdef.DSC64_K_DTYPE_ZI_swigconstant(_dscdef)
DSC64_K_DTYPE_ZI = _dscdef.DSC64_K_DTYPE_ZI

_dscdef.DSC_K_DTYPE_ZEM_swigconstant(_dscdef)
DSC_K_DTYPE_ZEM = _dscdef.DSC_K_DTYPE_ZEM

_dscdef.DSC64_K_DTYPE_ZEM_swigconstant(_dscdef)
DSC64_K_DTYPE_ZEM = _dscdef.DSC64_K_DTYPE_ZEM

_dscdef.DSC_K_DTYPE_DSC_swigconstant(_dscdef)
DSC_K_DTYPE_DSC = _dscdef.DSC_K_DTYPE_DSC

_dscdef.DSC64_K_DTYPE_DSC_swigconstant(_dscdef)
DSC64_K_DTYPE_DSC = _dscdef.DSC64_K_DTYPE_DSC

_dscdef.DSC_K_DTYPE_BPV_swigconstant(_dscdef)
DSC_K_DTYPE_BPV = _dscdef.DSC_K_DTYPE_BPV

_dscdef.DSC64_K_DTYPE_BPV_swigconstant(_dscdef)
DSC64_K_DTYPE_BPV = _dscdef.DSC64_K_DTYPE_BPV

_dscdef.DSC_K_DTYPE_BLV_swigconstant(_dscdef)
DSC_K_DTYPE_BLV = _dscdef.DSC_K_DTYPE_BLV

_dscdef.DSC64_K_DTYPE_BLV_swigconstant(_dscdef)
DSC64_K_DTYPE_BLV = _dscdef.DSC64_K_DTYPE_BLV

_dscdef.DSC_K_DTYPE_ADT_swigconstant(_dscdef)
DSC_K_DTYPE_ADT = _dscdef.DSC_K_DTYPE_ADT

_dscdef.DSC64_K_DTYPE_ADT_swigconstant(_dscdef)
DSC64_K_DTYPE_ADT = _dscdef.DSC64_K_DTYPE_ADT

_dscdef.DSC_K_DTYPE_CAD_swigconstant(_dscdef)
DSC_K_DTYPE_CAD = _dscdef.DSC_K_DTYPE_CAD

_dscdef.DSC64_K_DTYPE_CAD_swigconstant(_dscdef)
DSC64_K_DTYPE_CAD = _dscdef.DSC64_K_DTYPE_CAD

_dscdef.DSC_K_DTYPE_ENT_swigconstant(_dscdef)
DSC_K_DTYPE_ENT = _dscdef.DSC_K_DTYPE_ENT

_dscdef.DSC64_K_DTYPE_ENT_swigconstant(_dscdef)
DSC64_K_DTYPE_ENT = _dscdef.DSC64_K_DTYPE_ENT

_dscdef.DSC_K_DTYPE_GBL_swigconstant(_dscdef)
DSC_K_DTYPE_GBL = _dscdef.DSC_K_DTYPE_GBL

_dscdef.DSC64_K_DTYPE_GBL_swigconstant(_dscdef)
DSC64_K_DTYPE_GBL = _dscdef.DSC64_K_DTYPE_GBL

_dscdef.DSC_K_DTYPE_EPT_swigconstant(_dscdef)
DSC_K_DTYPE_EPT = _dscdef.DSC_K_DTYPE_EPT

_dscdef.DSC64_K_DTYPE_EPT_swigconstant(_dscdef)
DSC64_K_DTYPE_EPT = _dscdef.DSC64_K_DTYPE_EPT

_dscdef.DSC_K_DTYPE_R11_swigconstant(_dscdef)
DSC_K_DTYPE_R11 = _dscdef.DSC_K_DTYPE_R11

_dscdef.DSC64_K_DTYPE_R11_swigconstant(_dscdef)
DSC64_K_DTYPE_R11 = _dscdef.DSC64_K_DTYPE_R11

_dscdef.DSC_K_DTYPE_FLD_swigconstant(_dscdef)
DSC_K_DTYPE_FLD = _dscdef.DSC_K_DTYPE_FLD

_dscdef.DSC64_K_DTYPE_FLD_swigconstant(_dscdef)
DSC64_K_DTYPE_FLD = _dscdef.DSC64_K_DTYPE_FLD

_dscdef.DSC_K_DTYPE_PCT_swigconstant(_dscdef)
DSC_K_DTYPE_PCT = _dscdef.DSC_K_DTYPE_PCT

_dscdef.DSC64_K_DTYPE_PCT_swigconstant(_dscdef)
DSC64_K_DTYPE_PCT = _dscdef.DSC64_K_DTYPE_PCT

_dscdef.DSC_K_DTYPE_DPC_swigconstant(_dscdef)
DSC_K_DTYPE_DPC = _dscdef.DSC_K_DTYPE_DPC

_dscdef.DSC64_K_DTYPE_DPC_swigconstant(_dscdef)
DSC64_K_DTYPE_DPC = _dscdef.DSC64_K_DTYPE_DPC

_dscdef.DSC_K_DTYPE_LBL_swigconstant(_dscdef)
DSC_K_DTYPE_LBL = _dscdef.DSC_K_DTYPE_LBL

_dscdef.DSC64_K_DTYPE_LBL_swigconstant(_dscdef)
DSC64_K_DTYPE_LBL = _dscdef.DSC64_K_DTYPE_LBL

_dscdef.DSC_K_DTYPE_SLB_swigconstant(_dscdef)
DSC_K_DTYPE_SLB = _dscdef.DSC_K_DTYPE_SLB

_dscdef.DSC64_K_DTYPE_SLB_swigconstant(_dscdef)
DSC64_K_DTYPE_SLB = _dscdef.DSC64_K_DTYPE_SLB

_dscdef.DSC_K_DTYPE_MOD_swigconstant(_dscdef)
DSC_K_DTYPE_MOD = _dscdef.DSC_K_DTYPE_MOD

_dscdef.DSC64_K_DTYPE_MOD_swigconstant(_dscdef)
DSC64_K_DTYPE_MOD = _dscdef.DSC64_K_DTYPE_MOD

_dscdef.DSC_K_DTYPE_EOM_swigconstant(_dscdef)
DSC_K_DTYPE_EOM = _dscdef.DSC_K_DTYPE_EOM

_dscdef.DSC64_K_DTYPE_EOM_swigconstant(_dscdef)
DSC64_K_DTYPE_EOM = _dscdef.DSC64_K_DTYPE_EOM

_dscdef.DSC_K_DTYPE_RTN_swigconstant(_dscdef)
DSC_K_DTYPE_RTN = _dscdef.DSC_K_DTYPE_RTN

_dscdef.DSC64_K_DTYPE_RTN_swigconstant(_dscdef)
DSC64_K_DTYPE_RTN = _dscdef.DSC64_K_DTYPE_RTN

_dscdef.DSC_K_DTYPE_EOR_swigconstant(_dscdef)
DSC_K_DTYPE_EOR = _dscdef.DSC_K_DTYPE_EOR

_dscdef.DSC64_K_DTYPE_EOR_swigconstant(_dscdef)
DSC64_K_DTYPE_EOR = _dscdef.DSC64_K_DTYPE_EOR

_dscdef.DSC_K_CLASS_Z_swigconstant(_dscdef)
DSC_K_CLASS_Z = _dscdef.DSC_K_CLASS_Z

_dscdef.DSC64_K_CLASS_Z_swigconstant(_dscdef)
DSC64_K_CLASS_Z = _dscdef.DSC64_K_CLASS_Z

_dscdef.DSC_K_CLASS_S_swigconstant(_dscdef)
DSC_K_CLASS_S = _dscdef.DSC_K_CLASS_S

_dscdef.DSC64_K_CLASS_S_swigconstant(_dscdef)
DSC64_K_CLASS_S = _dscdef.DSC64_K_CLASS_S

_dscdef.DSC_K_CLASS_D_swigconstant(_dscdef)
DSC_K_CLASS_D = _dscdef.DSC_K_CLASS_D

_dscdef.DSC64_K_CLASS_D_swigconstant(_dscdef)
DSC64_K_CLASS_D = _dscdef.DSC64_K_CLASS_D

_dscdef.DSC_K_CLASS_V_swigconstant(_dscdef)
DSC_K_CLASS_V = _dscdef.DSC_K_CLASS_V

_dscdef.DSC64_K_CLASS_V_swigconstant(_dscdef)
DSC64_K_CLASS_V = _dscdef.DSC64_K_CLASS_V

_dscdef.DSC_K_CLASS_A_swigconstant(_dscdef)
DSC_K_CLASS_A = _dscdef.DSC_K_CLASS_A

_dscdef.DSC64_K_CLASS_A_swigconstant(_dscdef)
DSC64_K_CLASS_A = _dscdef.DSC64_K_CLASS_A

_dscdef.DSC_K_CLASS_P_swigconstant(_dscdef)
DSC_K_CLASS_P = _dscdef.DSC_K_CLASS_P

_dscdef.DSC64_K_CLASS_P_swigconstant(_dscdef)
DSC64_K_CLASS_P = _dscdef.DSC64_K_CLASS_P

_dscdef.DSC_K_CLASS_PI_swigconstant(_dscdef)
DSC_K_CLASS_PI = _dscdef.DSC_K_CLASS_PI

_dscdef.DSC64_K_CLASS_PI_swigconstant(_dscdef)
DSC64_K_CLASS_PI = _dscdef.DSC64_K_CLASS_PI

_dscdef.DSC_K_CLASS_J_swigconstant(_dscdef)
DSC_K_CLASS_J = _dscdef.DSC_K_CLASS_J

_dscdef.DSC64_K_CLASS_J_swigconstant(_dscdef)
DSC64_K_CLASS_J = _dscdef.DSC64_K_CLASS_J

_dscdef.DSC_K_CLASS_JI_swigconstant(_dscdef)
DSC_K_CLASS_JI = _dscdef.DSC_K_CLASS_JI

_dscdef.DSC_K_CLASS_SD_swigconstant(_dscdef)
DSC_K_CLASS_SD = _dscdef.DSC_K_CLASS_SD

_dscdef.DSC64_K_CLASS_SD_swigconstant(_dscdef)
DSC64_K_CLASS_SD = _dscdef.DSC64_K_CLASS_SD

_dscdef.DSC_K_CLASS_NCA_swigconstant(_dscdef)
DSC_K_CLASS_NCA = _dscdef.DSC_K_CLASS_NCA

_dscdef.DSC64_K_CLASS_NCA_swigconstant(_dscdef)
DSC64_K_CLASS_NCA = _dscdef.DSC64_K_CLASS_NCA

_dscdef.DSC_K_CLASS_VS_swigconstant(_dscdef)
DSC_K_CLASS_VS = _dscdef.DSC_K_CLASS_VS

_dscdef.DSC64_K_CLASS_VS_swigconstant(_dscdef)
DSC64_K_CLASS_VS = _dscdef.DSC64_K_CLASS_VS

_dscdef.DSC_K_CLASS_VSA_swigconstant(_dscdef)
DSC_K_CLASS_VSA = _dscdef.DSC_K_CLASS_VSA

_dscdef.DSC64_K_CLASS_VSA_swigconstant(_dscdef)
DSC64_K_CLASS_VSA = _dscdef.DSC64_K_CLASS_VSA

_dscdef.DSC_K_CLASS_UBS_swigconstant(_dscdef)
DSC_K_CLASS_UBS = _dscdef.DSC_K_CLASS_UBS

_dscdef.DSC64_K_CLASS_UBS_swigconstant(_dscdef)
DSC64_K_CLASS_UBS = _dscdef.DSC64_K_CLASS_UBS

_dscdef.DSC_K_CLASS_UBA_swigconstant(_dscdef)
DSC_K_CLASS_UBA = _dscdef.DSC_K_CLASS_UBA

_dscdef.DSC64_K_CLASS_UBA_swigconstant(_dscdef)
DSC64_K_CLASS_UBA = _dscdef.DSC64_K_CLASS_UBA

_dscdef.DSC_K_CLASS_SB_swigconstant(_dscdef)
DSC_K_CLASS_SB = _dscdef.DSC_K_CLASS_SB

_dscdef.DSC64_K_CLASS_SB_swigconstant(_dscdef)
DSC64_K_CLASS_SB = _dscdef.DSC64_K_CLASS_SB

_dscdef.DSC_K_CLASS_UBSB_swigconstant(_dscdef)
DSC_K_CLASS_UBSB = _dscdef.DSC_K_CLASS_UBSB

_dscdef.DSC64_K_CLASS_UBSB_swigconstant(_dscdef)
DSC64_K_CLASS_UBSB = _dscdef.DSC64_K_CLASS_UBSB

_dscdef.DSC_K_CLASS_BFA_swigconstant(_dscdef)
DSC_K_CLASS_BFA = _dscdef.DSC_K_CLASS_BFA

_dscdef.DSC_S_DSCDEF_swigconstant(_dscdef)
DSC_S_DSCDEF = _dscdef.DSC_S_DSCDEF

_dscdef.DSC_S_DSCDEF1_swigconstant(_dscdef)
DSC_S_DSCDEF1 = _dscdef.DSC_S_DSCDEF1

_dscdef.DSC_K_Z_BLN_swigconstant(_dscdef)
DSC_K_Z_BLN = _dscdef.DSC_K_Z_BLN

_dscdef.DSC_C_Z_BLN_swigconstant(_dscdef)
DSC_C_Z_BLN = _dscdef.DSC_C_Z_BLN

_dscdef.DSC_K_S_BLN_swigconstant(_dscdef)
DSC_K_S_BLN = _dscdef.DSC_K_S_BLN

_dscdef.DSC_C_S_BLN_swigconstant(_dscdef)
DSC_C_S_BLN = _dscdef.DSC_C_S_BLN

_dscdef.DSC_K_D_BLN_swigconstant(_dscdef)
DSC_K_D_BLN = _dscdef.DSC_K_D_BLN

_dscdef.DSC_C_D_BLN_swigconstant(_dscdef)
DSC_C_D_BLN = _dscdef.DSC_C_D_BLN

_dscdef.DSC_K_P_BLN_swigconstant(_dscdef)
DSC_K_P_BLN = _dscdef.DSC_K_P_BLN

_dscdef.DSC_C_P_BLN_swigconstant(_dscdef)
DSC_C_P_BLN = _dscdef.DSC_C_P_BLN

_dscdef.DSC_K_J_BLN_swigconstant(_dscdef)
DSC_K_J_BLN = _dscdef.DSC_K_J_BLN

_dscdef.DSC_C_J_BLN_swigconstant(_dscdef)
DSC_C_J_BLN = _dscdef.DSC_C_J_BLN

_dscdef.DSC_K_VS_BLN_swigconstant(_dscdef)
DSC_K_VS_BLN = _dscdef.DSC_K_VS_BLN

_dscdef.DSC_C_VS_BLN_swigconstant(_dscdef)
DSC_C_VS_BLN = _dscdef.DSC_C_VS_BLN

_dscdef.DSC_S_DSCDEF2_swigconstant(_dscdef)
DSC_S_DSCDEF2 = _dscdef.DSC_S_DSCDEF2

_dscdef.DSC_K_UBS_BLN_swigconstant(_dscdef)
DSC_K_UBS_BLN = _dscdef.DSC_K_UBS_BLN

_dscdef.DSC_C_UBS_BLN_swigconstant(_dscdef)
DSC_C_UBS_BLN = _dscdef.DSC_C_UBS_BLN

_dscdef.DSC_S_DSCDEF3_swigconstant(_dscdef)
DSC_S_DSCDEF3 = _dscdef.DSC_S_DSCDEF3

_dscdef.DSC_S_DSCDEF4_swigconstant(_dscdef)
DSC_S_DSCDEF4 = _dscdef.DSC_S_DSCDEF4

_dscdef.DSC_K_SD_BLN_swigconstant(_dscdef)
DSC_K_SD_BLN = _dscdef.DSC_K_SD_BLN

_dscdef.DSC_C_SD_BLN_swigconstant(_dscdef)
DSC_C_SD_BLN = _dscdef.DSC_C_SD_BLN

_dscdef.DSC_S_DSCDEF5_swigconstant(_dscdef)
DSC_S_DSCDEF5 = _dscdef.DSC_S_DSCDEF5

_dscdef.DSC_S_DSCDEF6_swigconstant(_dscdef)
DSC_S_DSCDEF6 = _dscdef.DSC_S_DSCDEF6

_dscdef.DSC_S_DSCDEF7_swigconstant(_dscdef)
DSC_S_DSCDEF7 = _dscdef.DSC_S_DSCDEF7

_dscdef.DSC_K_PI_BLN_swigconstant(_dscdef)
DSC_K_PI_BLN = _dscdef.DSC_K_PI_BLN

_dscdef.DSC_C_PI_BLN_swigconstant(_dscdef)
DSC_C_PI_BLN = _dscdef.DSC_C_PI_BLN

_dscdef.DSC_K_JI_BLN_swigconstant(_dscdef)
DSC_K_JI_BLN = _dscdef.DSC_K_JI_BLN

_dscdef.DSC_C_JI_BLN_swigconstant(_dscdef)
DSC_C_JI_BLN = _dscdef.DSC_C_JI_BLN

_dscdef.DSC_S_DSCDEF8_swigconstant(_dscdef)
DSC_S_DSCDEF8 = _dscdef.DSC_S_DSCDEF8

_dscdef.DSC_S_DSCDEF9_swigconstant(_dscdef)
DSC_S_DSCDEF9 = _dscdef.DSC_S_DSCDEF9

_dscdef.DSC_S_DSCDEF10_swigconstant(_dscdef)
DSC_S_DSCDEF10 = _dscdef.DSC_S_DSCDEF10

_dscdef.DSC64_S_DSCDEF64_swigconstant(_dscdef)
DSC64_S_DSCDEF64 = _dscdef.DSC64_S_DSCDEF64

_dscdef.DSC64_S_LENGTH_swigconstant(_dscdef)
DSC64_S_LENGTH = _dscdef.DSC64_S_LENGTH

_dscdef.DSC64_S_DSCDEF1_64_swigconstant(_dscdef)
DSC64_S_DSCDEF1_64 = _dscdef.DSC64_S_DSCDEF1_64

_dscdef.DSC64_S_MAXSTRLEN_swigconstant(_dscdef)
DSC64_S_MAXSTRLEN = _dscdef.DSC64_S_MAXSTRLEN

_dscdef.DSC64_S_POINTER_swigconstant(_dscdef)
DSC64_S_POINTER = _dscdef.DSC64_S_POINTER

_dscdef.DSC64_K_Z_BLN_swigconstant(_dscdef)
DSC64_K_Z_BLN = _dscdef.DSC64_K_Z_BLN

_dscdef.DSC64_C_Z_BLN_swigconstant(_dscdef)
DSC64_C_Z_BLN = _dscdef.DSC64_C_Z_BLN

_dscdef.DSC64_K_S_BLN_swigconstant(_dscdef)
DSC64_K_S_BLN = _dscdef.DSC64_K_S_BLN

_dscdef.DSC64_C_S_BLN_swigconstant(_dscdef)
DSC64_C_S_BLN = _dscdef.DSC64_C_S_BLN

_dscdef.DSC64_K_D_BLN_swigconstant(_dscdef)
DSC64_K_D_BLN = _dscdef.DSC64_K_D_BLN

_dscdef.DSC64_C_D_BLN_swigconstant(_dscdef)
DSC64_C_D_BLN = _dscdef.DSC64_C_D_BLN

_dscdef.DSC64_K_P_BLN_swigconstant(_dscdef)
DSC64_K_P_BLN = _dscdef.DSC64_K_P_BLN

_dscdef.DSC64_C_P_BLN_swigconstant(_dscdef)
DSC64_C_P_BLN = _dscdef.DSC64_C_P_BLN

_dscdef.DSC64_K_J_BLN_swigconstant(_dscdef)
DSC64_K_J_BLN = _dscdef.DSC64_K_J_BLN

_dscdef.DSC64_C_J_BLN_swigconstant(_dscdef)
DSC64_C_J_BLN = _dscdef.DSC64_C_J_BLN

_dscdef.DSC64_K_VS_BLN_swigconstant(_dscdef)
DSC64_K_VS_BLN = _dscdef.DSC64_K_VS_BLN

_dscdef.DSC64_C_VS_BLN_swigconstant(_dscdef)
DSC64_C_VS_BLN = _dscdef.DSC64_C_VS_BLN

_dscdef.DSC64_S_DSCDEF2_64_swigconstant(_dscdef)
DSC64_S_DSCDEF2_64 = _dscdef.DSC64_S_DSCDEF2_64

_dscdef.DSC64_S_BASE_swigconstant(_dscdef)
DSC64_S_BASE = _dscdef.DSC64_S_BASE

_dscdef.DSC64_K_UBS_BLN_swigconstant(_dscdef)
DSC64_K_UBS_BLN = _dscdef.DSC64_K_UBS_BLN

_dscdef.DSC64_C_UBS_BLN_swigconstant(_dscdef)
DSC64_C_UBS_BLN = _dscdef.DSC64_C_UBS_BLN

_dscdef.DSC64_S_DSCDEF3_64_swigconstant(_dscdef)
DSC64_S_DSCDEF3_64 = _dscdef.DSC64_S_DSCDEF3_64

_dscdef.DSC64_S_POS_swigconstant(_dscdef)
DSC64_S_POS = _dscdef.DSC64_S_POS

_dscdef.DSC64_K_SD_BLN_swigconstant(_dscdef)
DSC64_K_SD_BLN = _dscdef.DSC64_K_SD_BLN

_dscdef.DSC64_C_SD_BLN_swigconstant(_dscdef)
DSC64_C_SD_BLN = _dscdef.DSC64_C_SD_BLN

_dscdef.DSC64_S_DSCDEF5_64_swigconstant(_dscdef)
DSC64_S_DSCDEF5_64 = _dscdef.DSC64_S_DSCDEF5_64

_dscdef.DSC64_S_ARSIZE_swigconstant(_dscdef)
DSC64_S_ARSIZE = _dscdef.DSC64_S_ARSIZE

_dscdef.DSC64_S_A0_swigconstant(_dscdef)
DSC64_S_A0 = _dscdef.DSC64_S_A0

_dscdef.DSC64_S_DSCDEF6_64_swigconstant(_dscdef)
DSC64_S_DSCDEF6_64 = _dscdef.DSC64_S_DSCDEF6_64

_dscdef.DSC64_S_V0_swigconstant(_dscdef)
DSC64_S_V0 = _dscdef.DSC64_S_V0

_dscdef.DSC64_S_S1_swigconstant(_dscdef)
DSC64_S_S1 = _dscdef.DSC64_S_S1

_dscdef.DSC64_S_S2_swigconstant(_dscdef)
DSC64_S_S2 = _dscdef.DSC64_S_S2

_dscdef.DSC64_S_DSCDEF7_64_swigconstant(_dscdef)
DSC64_S_DSCDEF7_64 = _dscdef.DSC64_S_DSCDEF7_64

_dscdef.DSC64_S_M1_swigconstant(_dscdef)
DSC64_S_M1 = _dscdef.DSC64_S_M1

_dscdef.DSC64_S_M2_swigconstant(_dscdef)
DSC64_S_M2 = _dscdef.DSC64_S_M2

_dscdef.DSC64_K_PI_BLN_swigconstant(_dscdef)
DSC64_K_PI_BLN = _dscdef.DSC64_K_PI_BLN

_dscdef.DSC64_C_PI_BLN_swigconstant(_dscdef)
DSC64_C_PI_BLN = _dscdef.DSC64_C_PI_BLN

_dscdef.DSC64_K_JI_BLN_swigconstant(_dscdef)
DSC64_K_JI_BLN = _dscdef.DSC64_K_JI_BLN

_dscdef.DSC64_C_JI_BLN_swigconstant(_dscdef)
DSC64_C_JI_BLN = _dscdef.DSC64_C_JI_BLN

_dscdef.DSC64_S_DSCDEF8_64_swigconstant(_dscdef)
DSC64_S_DSCDEF8_64 = _dscdef.DSC64_S_DSCDEF8_64

_dscdef.DSC64_S_FRAME_swigconstant(_dscdef)
DSC64_S_FRAME = _dscdef.DSC64_S_FRAME

_dscdef.DSC64_S_DSCDEF9_64_swigconstant(_dscdef)
DSC64_S_DSCDEF9_64 = _dscdef.DSC64_S_DSCDEF9_64

_dscdef.DSC64_S_SB_L1_swigconstant(_dscdef)
DSC64_S_SB_L1 = _dscdef.DSC64_S_SB_L1

_dscdef.DSC64_S_SB_U1_swigconstant(_dscdef)
DSC64_S_SB_U1 = _dscdef.DSC64_S_SB_U1

_dscdef.DSC64_S_DSCDEF10_64_swigconstant(_dscdef)
DSC64_S_DSCDEF10_64 = _dscdef.DSC64_S_DSCDEF10_64

_dscdef.DSC64_S_UBSB_L1_swigconstant(_dscdef)
DSC64_S_UBSB_L1 = _dscdef.DSC64_S_UBSB_L1

_dscdef.DSC64_S_UBSB_U1_swigconstant(_dscdef)
DSC64_S_UBSB_U1 = _dscdef.DSC64_S_UBSB_U1
# This file is compatible with both classic and new-style classes.


