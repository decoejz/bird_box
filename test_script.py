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

    #@unittest.skip('Em desenvolvimento.')
    def test_viu(self):
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

        post_id = acha_post(conn, titulo=titulo, email=email)

        #Teste que verifica se uma visualizacao foi inserida corretamente
        target = adiciona_viu(conn, email="ayres@linkadinho.inspermon.br", id_post=post_id[0], so="ubuntu", ip="192.168.0.1", browser="Internet Explorer")
        self.assertIsNone(target)

        #Testa se e possivel encontrar a visualizacao
        target = acha_viu(conn, email="ayres@linkadinho.inspermon.br", id_post=post_id[0])
        self.assertIsNotNone(target)

    #@unittest.skip('Em desenvolvimento.')
    def test_desable_all(self):
        conn = self.__class__.connection
        
        titulo = "pudim amassado"
        texto  = "era uma vez um pudim apaixonado por #dragões como o @ayres@linkadinho.inspermon.br e o @john@smith.com"
        url    = "https://i.ytimg.com/vi/vdBFctcEzOM/maxresdefault.jpg"
        email  = "wesgas@al.insper.edu"
        nome   = "André"
        cidade = "Orlândia"
        
        adiciona_usuario(conn, nome=nome, email=email, cidade=cidade)
        adiciona_usuario(conn, nome="ayrezard", email="ayres@linkadinho.inspermon.br",cidade="megadadolis")
        adiciona_usuario(conn, nome="John Smith", email="john@smith.com", cidade="TARDIS")

        adiciona_post(conn,titulo=titulo, texto=texto, url = url, email=email)

        post_id = acha_post(conn, titulo=titulo, email=email)
        post_id = post_id[0]
        adiciona_viu(conn, email="ayres@linkadinho.inspermon.br", id_post=post_id, so="ubuntu", ip="192.168.0.1", browser="Internet Explorer")
        adiciona_viu(conn, email="john@smith.com", id_post=post_id, so="yana", ip="13", browser="Tardis Explorer")
        
        #Testa a remocao de um post e suas dependencias
        target = remove_post(conn, titulo=titulo, email=email)
        self.assertIsNone(target)

        atividade = post_esta_ativo(conn, titulo=titulo, email=email)
        self.assertEqual(atividade, 0)

        atividade = acha_tag(conn, post_id)
        for i in atividade:
            self.assertEqual(i[2], 0)

        atividade = acha_shout(conn, post_id)
        for i in atividade:
            self.assertEqual(i[2], 0)

        atividade = acha_viu(conn, email="john@smith.com", id_post=post_id)
        self.assertEqual(atividade[6], 0)

        atividade = acha_viu(conn, email="ayres@linkadinho.inspermon.br", id_post=post_id)
        self.assertEqual(atividade[6], 0)

    # @unittest.skip('Em desenvolvimento.')
    def test_lista_usuario(self):
        conn = self.__class__.connection
        
        nome   = "André"
        cidade = "Orlândia"
        usuarios_email = ["wesgas@al.insper.edu", "ayres@linkadinho.inspermon.br", "john@smith.com", "han@solo.com"]
        
        #Testa que ainda nao tem usuarios
        target = lista_usuarios(conn)
        self.assertFalse(target)

        adiciona_usuario(conn, nome=nome, email=usuarios_email[0], cidade=cidade)
        adiciona_usuario(conn, nome="ayrezard", email=usuarios_email[1],cidade="megadadolis")
        adiciona_usuario(conn, nome="John Smith", email=usuarios_email[2], cidade="TARDIS")
        adiciona_usuario(conn, nome="Han", email=usuarios_email[3], cidade="Corellia")

        target = lista_usuarios(conn)
        self.assertCountEqual(target, usuarios_email)

        for i in usuarios_email:
            remove_usuario(conn, i)

        target = lista_usuarios(conn)
        self.assertFalse(target)

    # @unittest.skip('Em desenvolvimento.')
    def test_lista_post(self):
        conn = self.__class__.connection
        
        titulo = "pudim amassado"
        texto  = "era uma vez um pudim apaixonado por #dragões como o @ayres@linkadinho.inspermon.br"
        url    = "https://i.ytimg.com/vi/vdBFctcEzOM/maxresdefault.jpg"
        nome   = "André"
        cidade = "Orlândia"
        usuarios_email = ["wesgas@al.insper.edu", "ayres@linkadinho.inspermon.br"]
        
        adiciona_usuario(conn, nome=nome, email=usuarios_email[0], cidade=cidade)
        adiciona_usuario(conn, nome="ayrezard", email=usuarios_email[1],cidade="megadadolis")
        
        target = lista_post(conn)
        self.assertFalse(target)

        adiciona_post(conn,titulo=titulo, texto=texto, url = url, email=usuarios_email[0])
        adiciona_post(conn,titulo="Tem uma cobra na minha bota", texto="Tinha uma cobra na bota do pobre menina", url = url, email=usuarios_email[1])

        posts_id = []
        posts_id.append(acha_post_id(conn, titulo, usuarios_email[0]))
        posts_id.append(acha_post_id(conn, "Tem uma cobra na minha bota", usuarios_email[1]))

        target = lista_post(conn)
        self.assertCountEqual(target, posts_id)

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
    #filenames = ["db_p1.sql", "trig_add_pas_v1.sql", "trigg_delete_post.sql"]
    os.chdir('sql')
    filenames = [entry for entry in os.listdir() 
        if os.path.isfile(entry) and re.match(r'.*_\d{3}\.sql', entry)]
    for filename in filenames:
        run_sql_script(filename)

if(__name__ == "__main__"):
    global config
    with open('config_testes.json') as f:
        config = json.load(f)
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main(verbosity=2)