#Baseado no código de Fabio Ayres
import pymysql

### ACOES RELACIONADAS AO USUARIO
def adiciona_usuario(conn, nome, email, cidade):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO usuario (nome, email, cidade) VALUES (%s, %s, %s)', (nome, email, cidade))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso inserir {nome} na tabela usuario')

def acha_usuario(conn, nome):
    with conn.cursor() as cursor:
        cursor.execute('SELECT email FROM usuario WHERE nome = %s', (nome))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None

def muda_nome_usuario(conn, email, novo_nome):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE usuario SET nome=%s where email=%s', (novo_nome, email))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso alterar nome do email {email} para {novo_nome} na tabela usuario')

def remove_usuario(conn, email):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM usuario WHERE email=%s', (email))

def lista_usuarios(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT email FROM usuario')
        res = cursor.fetchall()
        perigos = tuple(x[0] for x in res)
        return perigos

### ACOES RELACIONADAS AS VISUALIZACOES
def adiciona_viu(conn, email, id_post, so, ip, browser):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO usuario_viu (email, id, so, ip, browser)\
                 VALUES (%s, %s, %s, %s, %s)', (email, id_post, so, ip, browser))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso adicionar visualizacao de {email} na tabela usuario_viu')

### ACOES RELACIONADAS A POSTS
def adiciona_post(conn, titulo, texto, url, email):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO post (titulo, texto, url, email)\
                 VALUES (%s, %s, %s, %s)', (titulo, texto, url, email))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso adicionar o post {titulo} de {email} na tabela post')