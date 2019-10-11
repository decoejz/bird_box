#Baseado no código de Fabio Ayres
import pymysql

### ACOES RELACIONADAS AO USUARIO
def adiciona_usuario(conn, nome, email, cidade):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO usuario (nome, email, cidade) VALUES (%s, %s, %s)', (nome, email, cidade))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso inserir {nome} na tabela usuario. Error: {e}')

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
            raise ValueError(f'Não posso alterar nome do email {email} para {novo_nome} na tabela usuario. Error: {e}')

def remove_usuario(conn, email):
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM usuario WHERE email=%s', (email))

def lista_usuarios(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT email FROM usuario')
        res = cursor.fetchall()
        usuarios = tuple(x[0] for x in res)
        return usuarios

def adiciona_preferencia(conn, passaro, email):
    with conn.cursor() as cursor:
        cursor.execute("""INSERT INTO preferencia
                            (email, nome)
                          VALUES 
                            (%s,%s)""", (email, passaro))

def acha_preferencia(conn, email, passaro):
    with conn.cursor() as cursor:
        cursor.execute("""SELECT 
                            * 
                          FROM
                            usuario INNER JOIN preferencia USING(email)
                            INNER JOIN passaro ON passaro.nome=preferencia.nome
                          WHERE
                            email=%s AND passaro.nome=%s
                          """, (email, passaro))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None


### ACOES RELACIONADAS AS VISUALIZACOES
def adiciona_viu(conn, email, id_post, so, ip, browser):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO usuario_viu (email, id, so, ip, browser)\
                 VALUES (%s, %s, %s, %s, %s)', (email, id_post, so, ip, browser))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso adicionar visualizacao de {email} na tabela usuario_viu. Error: {e}')

### ACOES RELACIONADAS A POSTS
def parser_texto(conn, texto, id):
    #Separa cada palavra do comentario para ser parseada e procurar as tags
    for word in texto.split():
        if(word[0] == '#'):
            try:
                adiciona_tag_passaro(conn, word[1:], id)
            except:
                pass    
        if(word[0] == '@'):
            try:
                adiciona_tag_usuario(conn, word[1:], id)
            except:
                pass 

def acha_post(conn, titulo, email):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM post WHERE titulo=%s AND email=%s", (titulo, email))
        res = cursor.fetchone()
        if res:
            return res
        else:
            return None
def post_esta_ativo(conn, titulo, email):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM post WHERE titulo=%s AND email=%s", (titulo, email))
        res = cursor.fetchone()
        if res:
            return res[4]
        else:
            return None

def acha_post_id(conn, titulo, email):
    with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM post WHERE titulo=%s AND email=%s", (titulo, email))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None

def adiciona_post(conn, titulo, texto, url, email):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO post (titulo, texto, url, email)\
                 VALUES (%s, %s, %s, %s)', (titulo, texto, url, email))
            cursor.execute('SELECT id FROM post WHERE id=LAST_INSERT_ID() LIMIT 1')
            id_post = cursor.fetchone()
            parser_texto(conn, texto, id_post)
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso adicionar o post {titulo} de {email} na tabela post; Erro: {e}')

def remove_post(conn, titulo, email):
    with conn.cursor() as cursor:
        cursor.execute("UPDATE post SET ativo = 0 WHERE titulo=%s AND email=%s", (titulo, email))

def acha_shout(conn, post_id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM tag_usuario WHERE id=%s", post_id)
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None

def adiciona_tag_usuario(conn, email, id):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO tag_usuario (email, id) VALUES (%s, %s)', (email, id))
        except pymysql.err.IntegrityError as e:
            print(f'Não posso adicionar a tag {email} na tabela tag_usuario. Error: {e}')

def acha_tag(conn, post_id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM tag_passaro WHERE id=%s", post_id)
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None

def adiciona_tag_passaro(conn, nome, id):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO tag_passaro (nome, id)\
                 VALUES (%s, %s)', (nome, id))
        except pymysql.err.IntegrityError as e:
            print(f'Não posso adicionar a tag {nome} na tabela tag_passaro. Error: {e}')