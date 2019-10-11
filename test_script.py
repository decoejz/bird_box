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
    
    def tearDown(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('ROLLBACK')

    def test_adiciona_usuario(self):
        conn = self.__class__.connection

        nome = "André"
        email="wesgas@al.insper.edu"
        cidade="Orlândia"
        
        adiciona_usuario(conn, nome=nome, email=email, cidade=cidade)

        target = acha_usuario(conn, nome)
        self.assertIsNotNone(target)

        target = acha_usuario(conn, "Vesly")
        self.assertIsNone(target)
    
    #@unittest.skip('Em desenvolvimento.')  
    def test_declara_preferencias(self):
        conn = self.__class__.connection

        email="wesgas@al.insper.edu"
        passaro = "pavão"
        nome = "André"
        cidade="Orlândia"
        
        adiciona_usuario(conn, nome=nome, email=email, cidade=cidade)
        adiciona_preferencia(conn, passaro=passaro, email=email)

        target = acha_preferencia(conn, email=email, passaro=passaro)
        self.assertIsNotNone(target)
       
    #@unittest.skip('Em desenvolvimento.')
    def test_adiciona_post(self):
        conn = self.__class__.connection
        
        titulo = "pudim amassado"
        texto  = "era uma vez um pudim apaixonado por #dragões como o @ayres@linkadinho.inspermon.br"
        url    = "https://i.ytimg.com/vi/vdBFctcEzOM/maxresdefault.jpg"
        email  = "wesgas@al.insper.edu"
        nome = "André"
        cidade="Orlândia"
        #Testa também os shouts e tags

        adiciona_usuario(conn, nome=nome, email=email, cidade=cidade)
        #Cria USER pra ser tageado
        adiciona_usuario(conn, nome="ayrezard", email="ayres@linkadinho.inspermon.br",cidade="megadadolis")
        
        adiciona_post(conn,titulo=titulo, texto=texto, url = url, email=email)
        
        # log = logging.getLogger("add_post")
        # log.debug("Message")
        post_id = acha_post_id(conn, titulo=titulo, email=email)
        self.assertIsNotNone(post_id)
        target = acha_shout(conn, post_id=post_id)
        self.assertEqual(target[0][0], "ayres@linkadinho.inspermon.br")

        target = acha_tag(conn, post_id)
        self.assertEqual(target[0][0],"dragões")

        target = acha_post(conn, titulo="Morreu", email=email)
        self.assertIsNone(target)

    #@unittest.skip('Em desenvolvimento.')
    def test_remove_post(self):
        conn = self.__class__.connection
        
        titulo = "pudim amassado"
        texto  = "era uma vez um pudim apaixonado por #dragões como o @ayres@linkadinho.inspermon.br"
        url    = "https://i.ytimg.com/vi/vdBFctcEzOM/maxresdefault.jpg"
        email  = "wesgas@al.insper.edu"
        nome   = "André"
        cidade = "Orlândia"
        
        adiciona_usuario(conn, nome=nome, email=email, cidade=cidade)
        adiciona_usuario(conn, nome="ayrezard", email="ayres@linkadinho.inspermon.br",cidade="megadadolis")

        adiciona_post(conn,titulo=titulo, texto=texto, url = url, email=email)

        target = acha_post(conn, titulo=titulo, email=email)
        self.assertIsNotNone(target)
        target = post_esta_ativo(conn, titulo=titulo, email=email)
        self.assertEqual(target, 1)
        
        remove_post(conn, titulo=titulo, email=email)
        #test para as relações e para as views
        target = post_esta_ativo(conn, titulo=titulo, email=email)
        self.assertEqual(target, 0)

    @unittest.skip('Em desenvolvimento.')
    def test_viu(self):
        pass

    @unittest.skip('Em desenvolvimento.')
    def test_desable_all(self):
        pass

    @unittest.skip('Em desenvolvimento.')
    def test_lista_post(self):
        pass

    @unittest.skip('Em desenvolvimento.')
    def test_lista_usuario(self):
        pass


def run_sql_script(filename):
    global config
    with open(filename, 'rb') as f:
        subprocess.run(
            [
                config['MYSQL'], 
                '-u', config['USER'], 
                '-p' + config['PASS'], 
                '-h', config['HOST']
            ], 
            stdin=f
        )

def setUpModule():
    filenames = ["db_p1.sql", "add_procedure_tag.sql", "trig_add_pas_v1.sql", "trigg_delete_post.sql"]
    for filename in filenames:
        run_sql_script(filename)

if(__name__ == "__main__"):
    global config
    with open('config_testes.json') as f:
        config = json.load(f)
    setUpModule()
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main(verbosity=2)