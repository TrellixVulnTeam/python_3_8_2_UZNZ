import sys
import unittest
import time
import os

from test.support import TESTFN

if sys.platform != 'OpenVMS':
    raise unittest.SkipTest('OpenVMS required')

import vms.decc as DECC
import vms.lib as LIB
import vms.syidef as SYIDEF
import vms.fabdef as FABDEF

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_record_file(self):
        """ tests write-read record file"""

        lines = [
            b"Line #1\n",
            b"\n",
            b"Line #3\n",
        ]
        
        fp = DECC.fopen(TESTFN, "w", "rfm=var")
        self.assertIsNotNone(fp)

        fd = DECC.fileno(fp)
        self.assertGreater(fd, 0)

        for line in lines:
            n = DECC.write(fd, line)
            self.assertEqual(n, len(line))
        DECC.fclose(fp)

        st = os.stat(TESTFN)
        self.assertEqual(st.st_fab_rfm, FABDEF.FAB_C_VAR)

        fp = DECC.fopen(TESTFN, "r")
        self.assertIsNotNone(fp)

        for line in lines:
            line_read = DECC.fgets(fp, 256)
            self.assertEqual(line.decode(), line_read)
        self.assertEqual(DECC.fgets(fp, 256), None)
        self.assertEqual(DECC.feof(fp), True)

        DECC.fclose(fp)

        os.remove(TESTFN)


    def test_dlopen_test(self):
        """ tests if shared image is accessible """
        self.assertEqual(1, DECC.dlopen_test("python$shr"))

    def test_fix_time(self):
        """ converts vms time to unix time (GMT) """
        self.assertEqual(1595490469, DECC.fix_time(51022072693664076))

    def test_from_vms(self):
        """ converts vms path to available unix paths """
        self.assertEqual( \
            list(map(lambda x: x.lower(), DECC.from_vms("python$root:[bin]python3.exe", 0))), \
            list(map(lambda x: x.lower(), DECC.from_vms("python$root:[bin]python3.*", 1))))

    def test_getenv(self):
        """ try to get PYTHONHOME """
        self.assertEqual('/python$root', DECC.getenv('PYTHONHOME', None))

    def test_sleep(self):
        """ sleep one second """
        start = time.time()
        DECC.sleep(1)
        diff = time.time() - start
        self.assertGreaterEqual(diff, 1)
        self.assertLess(diff, 1.01)

    def test_sysconf(self):
        """ try to get PAGESIZE """
        pagesize_decc = DECC.sysconf(DECC._SC_PAGESIZE)
        status, pagesize_sys, _ = LIB.getsyi(SYIDEF.SYI__PAGE_SIZE, None)
        self.assertEqual(1, status)
        pagesize_sys = int(pagesize_sys)
        self.assertEqual(pagesize_decc, pagesize_sys)

    def test_to_vms(self):
        """ converts unix path to vms path """
        self.assertEqual( \
            list(map(lambda x: x.lower(), DECC.to_vms('/python$root/bin/python3.exe', 0, 0))), \
            list(map(lambda x: x.lower(), DECC.to_vms('/python$root/bin/python3.*', 1, 0))))

    def test_unixtime(self):
        """ converts vms time to unix time (using time zone) """
        DECC.unixtime(51022072693664076)

    def test_vmstime(self):
        """ converts unix time to vms time (GMT) """
        self.assertEqual(35067168000000000, DECC.vmstime(0))
        self.assertEqual(0, DECC.fix_time(DECC.vmstime(0)))

if __name__ == "__main__":
    unittest.main(verbosity=2)
