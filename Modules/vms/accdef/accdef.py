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
            fp, pathname, description = imp.find_module('_accdef', [dirname(__file__)])
        except ImportError:
            import _accdef
            return _accdef
        if fp is not None:
            try:
                _mod = imp.load_module('_accdef', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _accdef = swig_import_helper()
    del swig_import_helper
else:
    import _accdef
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



_accdef.ACC_K_TERMLEN_swigconstant(_accdef)
ACC_K_TERMLEN = _accdef.ACC_K_TERMLEN

_accdef.ACC_C_TERMLEN_swigconstant(_accdef)
ACC_C_TERMLEN = _accdef.ACC_C_TERMLEN

_accdef.ACC_K_JOB_LEN_swigconstant(_accdef)
ACC_K_JOB_LEN = _accdef.ACC_K_JOB_LEN

_accdef.ACC_C_JOB_LEN_swigconstant(_accdef)
ACC_C_JOB_LEN = _accdef.ACC_C_JOB_LEN

_accdef.ACC_S_ACCDEF_swigconstant(_accdef)
ACC_S_ACCDEF = _accdef.ACC_S_ACCDEF

_accdef.ACC_S_TERMTIME_swigconstant(_accdef)
ACC_S_TERMTIME = _accdef.ACC_S_TERMTIME

_accdef.ACC_S_ACCOUNT_swigconstant(_accdef)
ACC_S_ACCOUNT = _accdef.ACC_S_ACCOUNT

_accdef.ACC_S_USERNAME_swigconstant(_accdef)
ACC_S_USERNAME = _accdef.ACC_S_USERNAME

_accdef.ACC_S_LOGIN_swigconstant(_accdef)
ACC_S_LOGIN = _accdef.ACC_S_LOGIN

_accdef.ACC_S_JOB_NAME_swigconstant(_accdef)
ACC_S_JOB_NAME = _accdef.ACC_S_JOB_NAME

_accdef.ACC_S_JOB_QUE_swigconstant(_accdef)
ACC_S_JOB_QUE = _accdef.ACC_S_JOB_QUE

_accdef.ACC_K_PRT_LEN_swigconstant(_accdef)
ACC_K_PRT_LEN = _accdef.ACC_K_PRT_LEN

_accdef.ACC_C_PRT_LEN_swigconstant(_accdef)
ACC_C_PRT_LEN = _accdef.ACC_C_PRT_LEN

_accdef.ACC_S_ACCDEF1_swigconstant(_accdef)
ACC_S_ACCDEF1 = _accdef.ACC_S_ACCDEF1

_accdef.ACC_S_QUETIME_swigconstant(_accdef)
ACC_S_QUETIME = _accdef.ACC_S_QUETIME

_accdef.ACC_S_PRT_NAME_swigconstant(_accdef)
ACC_S_PRT_NAME = _accdef.ACC_S_PRT_NAME

_accdef.ACC_S_PRT_QUE_swigconstant(_accdef)
ACC_S_PRT_QUE = _accdef.ACC_S_PRT_QUE

_accdef.ACC_K_INS_LEN_swigconstant(_accdef)
ACC_K_INS_LEN = _accdef.ACC_K_INS_LEN

_accdef.ACC_C_INS_LEN_swigconstant(_accdef)
ACC_C_INS_LEN = _accdef.ACC_C_INS_LEN

_accdef.ACC_K_PRCTRM_swigconstant(_accdef)
ACC_K_PRCTRM = _accdef.ACC_K_PRCTRM

_accdef.ACC_K_BATTRM_swigconstant(_accdef)
ACC_K_BATTRM = _accdef.ACC_K_BATTRM

_accdef.ACC_K_INTTRM_swigconstant(_accdef)
ACC_K_INTTRM = _accdef.ACC_K_INTTRM

_accdef.ACC_K_LOGTRM_swigconstant(_accdef)
ACC_K_LOGTRM = _accdef.ACC_K_LOGTRM

_accdef.ACC_K_IMGTRM_swigconstant(_accdef)
ACC_K_IMGTRM = _accdef.ACC_K_IMGTRM

_accdef.ACC_K_SUBTRM_swigconstant(_accdef)
ACC_K_SUBTRM = _accdef.ACC_K_SUBTRM

_accdef.ACC_K_DETTRM_swigconstant(_accdef)
ACC_K_DETTRM = _accdef.ACC_K_DETTRM

_accdef.ACC_K_NETTRM_swigconstant(_accdef)
ACC_K_NETTRM = _accdef.ACC_K_NETTRM

_accdef.ACC_K_PRTJOB_swigconstant(_accdef)
ACC_K_PRTJOB = _accdef.ACC_K_PRTJOB

_accdef.ACC_K_INSMSG_swigconstant(_accdef)
ACC_K_INSMSG = _accdef.ACC_K_INSMSG

_accdef.ACC_K_INSMESG_swigconstant(_accdef)
ACC_K_INSMESG = _accdef.ACC_K_INSMESG

_accdef.ACC_K_NEWFILE_swigconstant(_accdef)
ACC_K_NEWFILE = _accdef.ACC_K_NEWFILE

_accdef.ACC_K_ENABACC_swigconstant(_accdef)
ACC_K_ENABACC = _accdef.ACC_K_ENABACC

_accdef.ACC_K_DISAACC_swigconstant(_accdef)
ACC_K_DISAACC = _accdef.ACC_K_DISAACC

_accdef.ACC_K_ENABSEL_swigconstant(_accdef)
ACC_K_ENABSEL = _accdef.ACC_K_ENABSEL

_accdef.ACC_K_DISASEL_swigconstant(_accdef)
ACC_K_DISASEL = _accdef.ACC_K_DISASEL

_accdef.ACC_S_ACCDEF2_swigconstant(_accdef)
ACC_S_ACCDEF2 = _accdef.ACC_S_ACCDEF2

_accdef.ACC_S_USER_DATA_swigconstant(_accdef)
ACC_S_USER_DATA = _accdef.ACC_S_USER_DATA
# This file is compatible with both classic and new-style classes.


