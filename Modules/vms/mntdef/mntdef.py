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
            fp, pathname, description = imp.find_module('_mntdef', [dirname(__file__)])
        except ImportError:
            import _mntdef
            return _mntdef
        if fp is not None:
            try:
                _mod = imp.load_module('_mntdef', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _mntdef = swig_import_helper()
    del swig_import_helper
else:
    import _mntdef
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



_mntdef.MNT_M_FOREIGN_swigconstant(_mntdef)
MNT_M_FOREIGN = _mntdef.MNT_M_FOREIGN

_mntdef.MNT_M_GROUP_swigconstant(_mntdef)
MNT_M_GROUP = _mntdef.MNT_M_GROUP

_mntdef.MNT_M_NOASSIST_swigconstant(_mntdef)
MNT_M_NOASSIST = _mntdef.MNT_M_NOASSIST

_mntdef.MNT_M_NODISKQ_swigconstant(_mntdef)
MNT_M_NODISKQ = _mntdef.MNT_M_NODISKQ

_mntdef.MNT_M_NOHDR3_swigconstant(_mntdef)
MNT_M_NOHDR3 = _mntdef.MNT_M_NOHDR3

_mntdef.MNT_M_NOLABEL_swigconstant(_mntdef)
MNT_M_NOLABEL = _mntdef.MNT_M_NOLABEL

_mntdef.MNT_M_NOWRITE_swigconstant(_mntdef)
MNT_M_NOWRITE = _mntdef.MNT_M_NOWRITE

_mntdef.MNT_M_OVR_ACCESS_swigconstant(_mntdef)
MNT_M_OVR_ACCESS = _mntdef.MNT_M_OVR_ACCESS

_mntdef.MNT_M_OVR_EXP_swigconstant(_mntdef)
MNT_M_OVR_EXP = _mntdef.MNT_M_OVR_EXP

_mntdef.MNT_M_OVR_IDENT_swigconstant(_mntdef)
MNT_M_OVR_IDENT = _mntdef.MNT_M_OVR_IDENT

_mntdef.MNT_M_OVR_SETID_swigconstant(_mntdef)
MNT_M_OVR_SETID = _mntdef.MNT_M_OVR_SETID

_mntdef.MNT_M_READCHECK_swigconstant(_mntdef)
MNT_M_READCHECK = _mntdef.MNT_M_READCHECK

_mntdef.MNT_M_SHARE_swigconstant(_mntdef)
MNT_M_SHARE = _mntdef.MNT_M_SHARE

_mntdef.MNT_M_MESSAGE_swigconstant(_mntdef)
MNT_M_MESSAGE = _mntdef.MNT_M_MESSAGE

_mntdef.MNT_M_SYSTEM_swigconstant(_mntdef)
MNT_M_SYSTEM = _mntdef.MNT_M_SYSTEM

_mntdef.MNT_M_WRITECHECK_swigconstant(_mntdef)
MNT_M_WRITECHECK = _mntdef.MNT_M_WRITECHECK

_mntdef.MNT_M_WRITETHRU_swigconstant(_mntdef)
MNT_M_WRITETHRU = _mntdef.MNT_M_WRITETHRU

_mntdef.MNT_M_NOCACHE_swigconstant(_mntdef)
MNT_M_NOCACHE = _mntdef.MNT_M_NOCACHE

_mntdef.MNT_M_OVR_LOCK_swigconstant(_mntdef)
MNT_M_OVR_LOCK = _mntdef.MNT_M_OVR_LOCK

_mntdef.MNT_M_NOMNTVER_swigconstant(_mntdef)
MNT_M_NOMNTVER = _mntdef.MNT_M_NOMNTVER

_mntdef.MNT_M_NOUNLOAD_swigconstant(_mntdef)
MNT_M_NOUNLOAD = _mntdef.MNT_M_NOUNLOAD

_mntdef.MNT_M_TAPE_DATA_WRITE_swigconstant(_mntdef)
MNT_M_TAPE_DATA_WRITE = _mntdef.MNT_M_TAPE_DATA_WRITE

_mntdef.MNT_M_NOCOPY_swigconstant(_mntdef)
MNT_M_NOCOPY = _mntdef.MNT_M_NOCOPY

_mntdef.MNT_M_NOAUTO_swigconstant(_mntdef)
MNT_M_NOAUTO = _mntdef.MNT_M_NOAUTO

_mntdef.MNT_M_INIT_ALL_swigconstant(_mntdef)
MNT_M_INIT_ALL = _mntdef.MNT_M_INIT_ALL

_mntdef.MNT_M_INIT_CONT_swigconstant(_mntdef)
MNT_M_INIT_CONT = _mntdef.MNT_M_INIT_CONT

_mntdef.MNT_M_OVR_VOLO_swigconstant(_mntdef)
MNT_M_OVR_VOLO = _mntdef.MNT_M_OVR_VOLO

_mntdef.MNT_M_INTERCHG_swigconstant(_mntdef)
MNT_M_INTERCHG = _mntdef.MNT_M_INTERCHG

_mntdef.MNT_M_CLUSTER_swigconstant(_mntdef)
MNT_M_CLUSTER = _mntdef.MNT_M_CLUSTER

_mntdef.MNT_M_NOREBUILD_swigconstant(_mntdef)
MNT_M_NOREBUILD = _mntdef.MNT_M_NOREBUILD

_mntdef.MNT_M_OVR_SHAMEM_swigconstant(_mntdef)
MNT_M_OVR_SHAMEM = _mntdef.MNT_M_OVR_SHAMEM

_mntdef.MNT_M_MULTI_VOL_swigconstant(_mntdef)
MNT_M_MULTI_VOL = _mntdef.MNT_M_MULTI_VOL

_mntdef.MNT2_M_DISKQ_swigconstant(_mntdef)
MNT2_M_DISKQ = _mntdef.MNT2_M_DISKQ

_mntdef.MNT2_M_COMPACTION_swigconstant(_mntdef)
MNT2_M_COMPACTION = _mntdef.MNT2_M_COMPACTION

_mntdef.MNT2_M_INCLUDE_swigconstant(_mntdef)
MNT2_M_INCLUDE = _mntdef.MNT2_M_INCLUDE

_mntdef.MNT2_M_PASS2_swigconstant(_mntdef)
MNT2_M_PASS2 = _mntdef.MNT2_M_PASS2

_mntdef.MNT2_M_OVR_NOFE_swigconstant(_mntdef)
MNT2_M_OVR_NOFE = _mntdef.MNT2_M_OVR_NOFE

_mntdef.MNT2_M_SCRATCH_swigconstant(_mntdef)
MNT2_M_SCRATCH = _mntdef.MNT2_M_SCRATCH

_mntdef.MNT2_M_CDROM_swigconstant(_mntdef)
MNT2_M_CDROM = _mntdef.MNT2_M_CDROM

_mntdef.MNT2_M_XAR_swigconstant(_mntdef)
MNT2_M_XAR = _mntdef.MNT2_M_XAR

_mntdef.MNT2_M_DSI_swigconstant(_mntdef)
MNT2_M_DSI = _mntdef.MNT2_M_DSI

_mntdef.MNT2_M_SUBSYSTEM_swigconstant(_mntdef)
MNT2_M_SUBSYSTEM = _mntdef.MNT2_M_SUBSYSTEM

_mntdef.MNT2_M_NOCOMPACTION_swigconstant(_mntdef)
MNT2_M_NOCOMPACTION = _mntdef.MNT2_M_NOCOMPACTION

_mntdef.MNT2_M_OVR_SECURITY_swigconstant(_mntdef)
MNT2_M_OVR_SECURITY = _mntdef.MNT2_M_OVR_SECURITY

_mntdef.MNT2_M_OVR_LIMITED_SEARCH_swigconstant(_mntdef)
MNT2_M_OVR_LIMITED_SEARCH = _mntdef.MNT2_M_OVR_LIMITED_SEARCH

_mntdef.MNT2_M_POOL_swigconstant(_mntdef)
MNT2_M_POOL = _mntdef.MNT2_M_POOL

_mntdef.MNT2_M_WLG_ENABLE_swigconstant(_mntdef)
MNT2_M_WLG_ENABLE = _mntdef.MNT2_M_WLG_ENABLE

_mntdef.MNT2_M_WLG_DISABLE_swigconstant(_mntdef)
MNT2_M_WLG_DISABLE = _mntdef.MNT2_M_WLG_DISABLE

_mntdef.MNT2_M_REQUIRE_MEMBERS_swigconstant(_mntdef)
MNT2_M_REQUIRE_MEMBERS = _mntdef.MNT2_M_REQUIRE_MEMBERS

_mntdef.MNT2_M_VERIFY_LABEL_swigconstant(_mntdef)
MNT2_M_VERIFY_LABEL = _mntdef.MNT2_M_VERIFY_LABEL

_mntdef.MNT2_M_FULL_MERGE_swigconstant(_mntdef)
MNT2_M_FULL_MERGE = _mntdef.MNT2_M_FULL_MERGE

_mntdef.MNT2_M_WRITE_FIRST_swigconstant(_mntdef)
MNT2_M_WRITE_FIRST = _mntdef.MNT2_M_WRITE_FIRST

_mntdef.MNT2_M_DCD_swigconstant(_mntdef)
MNT2_M_DCD = _mntdef.MNT2_M_DCD

_mntdef.MNT2_M_NODCD_swigconstant(_mntdef)
MNT2_M_NODCD = _mntdef.MNT2_M_NODCD

_mntdef.MNT2_M_LOCAL_HOST_swigconstant(_mntdef)
MNT2_M_LOCAL_HOST = _mntdef.MNT2_M_LOCAL_HOST

_mntdef.MNT2_M_FACTOR_swigconstant(_mntdef)
MNT2_M_FACTOR = _mntdef.MNT2_M_FACTOR

_mntdef.MNT2_M_PRIORITY_swigconstant(_mntdef)
MNT2_M_PRIORITY = _mntdef.MNT2_M_PRIORITY

_mntdef.MNT__DEVNAM_swigconstant(_mntdef)
MNT__DEVNAM = _mntdef.MNT__DEVNAM

_mntdef.MNT__VOLNAM_swigconstant(_mntdef)
MNT__VOLNAM = _mntdef.MNT__VOLNAM

_mntdef.MNT__LOGNAM_swigconstant(_mntdef)
MNT__LOGNAM = _mntdef.MNT__LOGNAM

_mntdef.MNT__FLAGS_swigconstant(_mntdef)
MNT__FLAGS = _mntdef.MNT__FLAGS

_mntdef.MNT__ACCESSED_swigconstant(_mntdef)
MNT__ACCESSED = _mntdef.MNT__ACCESSED

_mntdef.MNT__PROCESSOR_swigconstant(_mntdef)
MNT__PROCESSOR = _mntdef.MNT__PROCESSOR

_mntdef.MNT__VOLSET_swigconstant(_mntdef)
MNT__VOLSET = _mntdef.MNT__VOLSET

_mntdef.MNT__BLOCKSIZE_swigconstant(_mntdef)
MNT__BLOCKSIZE = _mntdef.MNT__BLOCKSIZE

_mntdef.MNT__DENSITY_swigconstant(_mntdef)
MNT__DENSITY = _mntdef.MNT__DENSITY

_mntdef.MNT__EXTENT_swigconstant(_mntdef)
MNT__EXTENT = _mntdef.MNT__EXTENT

_mntdef.MNT__FILEID_swigconstant(_mntdef)
MNT__FILEID = _mntdef.MNT__FILEID

_mntdef.MNT__LIMIT_swigconstant(_mntdef)
MNT__LIMIT = _mntdef.MNT__LIMIT

_mntdef.MNT__OWNER_swigconstant(_mntdef)
MNT__OWNER = _mntdef.MNT__OWNER

_mntdef.MNT__VPROT_swigconstant(_mntdef)
MNT__VPROT = _mntdef.MNT__VPROT

_mntdef.MNT__QUOTA_swigconstant(_mntdef)
MNT__QUOTA = _mntdef.MNT__QUOTA

_mntdef.MNT__RECORDSIZ_swigconstant(_mntdef)
MNT__RECORDSIZ = _mntdef.MNT__RECORDSIZ

_mntdef.MNT__WINDOW_swigconstant(_mntdef)
MNT__WINDOW = _mntdef.MNT__WINDOW

_mntdef.MNT__EXTENSION_swigconstant(_mntdef)
MNT__EXTENSION = _mntdef.MNT__EXTENSION

_mntdef.MNT__VISUAL_ID_swigconstant(_mntdef)
MNT__VISUAL_ID = _mntdef.MNT__VISUAL_ID

_mntdef.MNT__COMMENT_swigconstant(_mntdef)
MNT__COMMENT = _mntdef.MNT__COMMENT

_mntdef.MNT__CLASS_swigconstant(_mntdef)
MNT__CLASS = _mntdef.MNT__CLASS

_mntdef.MNT__UNUSED2_swigconstant(_mntdef)
MNT__UNUSED2 = _mntdef.MNT__UNUSED2

_mntdef.MNT__ACCPTNAM_swigconstant(_mntdef)
MNT__ACCPTNAM = _mntdef.MNT__ACCPTNAM

_mntdef.MNT__SHACOPY_BUF_swigconstant(_mntdef)
MNT__SHACOPY_BUF = _mntdef.MNT__SHACOPY_BUF

_mntdef.MNT__SHANAM_swigconstant(_mntdef)
MNT__SHANAM = _mntdef.MNT__SHANAM

_mntdef.MNT__SHAMEM_swigconstant(_mntdef)
MNT__SHAMEM = _mntdef.MNT__SHAMEM

_mntdef.MNT__SHAMEM_MGCOPY_swigconstant(_mntdef)
MNT__SHAMEM_MGCOPY = _mntdef.MNT__SHAMEM_MGCOPY

_mntdef.MNT__SHAMEM_COPY_swigconstant(_mntdef)
MNT__SHAMEM_COPY = _mntdef.MNT__SHAMEM_COPY

_mntdef.MNT__PRFD_PATH_swigconstant(_mntdef)
MNT__PRFD_PATH = _mntdef.MNT__PRFD_PATH

_mntdef.MNT__ASSIGNMENT_UNIT_swigconstant(_mntdef)
MNT__ASSIGNMENT_UNIT = _mntdef.MNT__ASSIGNMENT_UNIT

_mntdef.MNT__CART_MEDIA_NAME_swigconstant(_mntdef)
MNT__CART_MEDIA_NAME = _mntdef.MNT__CART_MEDIA_NAME

_mntdef.MNT__CARTRIDGE_NAME_swigconstant(_mntdef)
MNT__CARTRIDGE_NAME = _mntdef.MNT__CARTRIDGE_NAME

_mntdef.MNT__CARTRIDGE_SIDE_swigconstant(_mntdef)
MNT__CARTRIDGE_SIDE = _mntdef.MNT__CARTRIDGE_SIDE

_mntdef.MNT__COLLECTION_swigconstant(_mntdef)
MNT__COLLECTION = _mntdef.MNT__COLLECTION

_mntdef.MNT__DEVICE_TYPE_swigconstant(_mntdef)
MNT__DEVICE_TYPE = _mntdef.MNT__DEVICE_TYPE

_mntdef.MNT__DISPOSITION_swigconstant(_mntdef)
MNT__DISPOSITION = _mntdef.MNT__DISPOSITION

_mntdef.MNT__LOCATION_swigconstant(_mntdef)
MNT__LOCATION = _mntdef.MNT__LOCATION

_mntdef.MNT__MEDIA_NAME_swigconstant(_mntdef)
MNT__MEDIA_NAME = _mntdef.MNT__MEDIA_NAME

_mntdef.MNT__UNUSED4_swigconstant(_mntdef)
MNT__UNUSED4 = _mntdef.MNT__UNUSED4

_mntdef.MNT__UNDEFINED_FAT_swigconstant(_mntdef)
MNT__UNDEFINED_FAT = _mntdef.MNT__UNDEFINED_FAT

_mntdef.MNT__UCS_swigconstant(_mntdef)
MNT__UCS = _mntdef.MNT__UCS

_mntdef.MNT__TAPE_EXPIRATION_swigconstant(_mntdef)
MNT__TAPE_EXPIRATION = _mntdef.MNT__TAPE_EXPIRATION

_mntdef.MNT__PRIORITY_swigconstant(_mntdef)
MNT__PRIORITY = _mntdef.MNT__PRIORITY

_mntdef.MNT__FACTOR_swigconstant(_mntdef)
MNT__FACTOR = _mntdef.MNT__FACTOR

_mntdef.MNT__WBM_SIZE_swigconstant(_mntdef)
MNT__WBM_SIZE = _mntdef.MNT__WBM_SIZE

_mntdef.MNT__DATA_swigconstant(_mntdef)
MNT__DATA = _mntdef.MNT__DATA

_mntdef.MNT__NODATA_swigconstant(_mntdef)
MNT__NODATA = _mntdef.MNT__NODATA

_mntdef.MNT__LAST_ITEM_CODE_swigconstant(_mntdef)
MNT__LAST_ITEM_CODE = _mntdef.MNT__LAST_ITEM_CODE

_mntdef.MNT_C_BASE_CARTRIDGE_swigconstant(_mntdef)
MNT_C_BASE_CARTRIDGE = _mntdef.MNT_C_BASE_CARTRIDGE

_mntdef.MNT_C_COMPOUND_CARTRIDGE_swigconstant(_mntdef)
MNT_C_COMPOUND_CARTRIDGE = _mntdef.MNT_C_COMPOUND_CARTRIDGE

_mntdef.MNT_C_PREASSIGNED_SIDE_swigconstant(_mntdef)
MNT_C_PREASSIGNED_SIDE = _mntdef.MNT_C_PREASSIGNED_SIDE

_mntdef.MNT_C_SIDE_swigconstant(_mntdef)
MNT_C_SIDE = _mntdef.MNT_C_SIDE

_mntdef.MNT_C_KEEP_swigconstant(_mntdef)
MNT_C_KEEP = _mntdef.MNT_C_KEEP

_mntdef.MNT_C_RELEASE_swigconstant(_mntdef)
MNT_C_RELEASE = _mntdef.MNT_C_RELEASE

_mntdef.MNT_S_MNTDEF_swigconstant(_mntdef)
MNT_S_MNTDEF = _mntdef.MNT_S_MNTDEF

_mntdef.UNFAT_S_UNDEFINED_FAT_swigconstant(_mntdef)
UNFAT_S_UNDEFINED_FAT = _mntdef.UNFAT_S_UNDEFINED_FAT
# This file is compatible with both classic and new-style classes.


