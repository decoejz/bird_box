import subprocess
import unittest
import logging
import sys
import json
import os
import os.path
import re
from projeto import *

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global config
        cls.connection = pymysql.connect(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASS'],
            database='bird_box'
        )
        
    
    @classmethod
    def tearDownClass(cls):
        cls.connection.close()
    
    def setUp(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('START TRANSACTION')
        with open('db_p1.sql', 'rb') as f:
            res = subprocess.run(f'mysql -u root -proot'.split(), stdin=f, capture_output=True)
            log = logging.getLogger("setup")
            log.debug(res)
    
    def tearDown(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('ROLLBACK')

    def test_adiciona_usuario(self):
        conn = self.__class__.connection

        adiciona_usuario(conn, nome="André", email="wesgas@al.insper.edu", cidade="Orlândia")

        target = acha_usuario(conn, "André")
        self.assertIsNotNone(target)

        target = acha_usuario(conn, "Vesly")
        self.assertIsNone(target)
        

if(__name__ == "__main__"):
    global config
    with open('config_tests.json') as f:
        config = json.load(f)
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()