import subprocess
import unittest
import logging
import sys

class TestCase(unittest.TestCase):
    def test_meu_teste(self):
        pass
    @classmethod
    def setUpClass(cls):
        with open('db_p1.sql', 'rb') as f:
            res = subprocess.run('mysql -u root -proot'.split(), stdin=f, capture_output=True)
            log = logging.getLogger("setup")
            log.debug(res)

if(__name__ == "__main__"):
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()