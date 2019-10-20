# Baseado no código de Fabio Ayres
import pymysql

# ACOES RELACIONADAS AO USUARIO


def adiciona_usuario(conn, nome, email, cidade):
    with conn.cursor() as cursor:
        cursor.execute(
            'INSERT INTO usuario (nome, email, cidade) VALUES (%s, %s, %s)', (nome, email, cidade))


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
        cursor.execute(
            'UPDATE usuario SET nome=%s where email=%s', (novo_nome, email))


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


# ACOES RELACIONADAS AS VISUALIZACOES
def adiciona_viu(conn, email, id_post, so, ip, browser):
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO usuario_viu (email, id, so, ip, browser)\
                 VALUES (%s, %s, %s, %s, %s)', (email, id_post, so, ip, browser))


def acha_viu(conn, email, id_post):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM usuario_viu WHERE email=%s AND id=%s", (email, id_post))
        res = cursor.fetchone()
        if res:
            return res
        else:
            return None

# ACOES RELACIONADAS A POSTS
def parser_texto(conn, texto, id):
    # Separa cada palavra do comentario para ser parseada e procurar as tags
    added = {"#": [], "@": []}
    for word in texto.split():
        if(word[0] == '#'):
            try:
                adiciona_tag_passaro(conn, word[1:], id)
                added["#"].append(word[1:])
            except:
                pass
        if(word[0] == '@'):
            try:
                adiciona_tag_usuario(conn, word[1:], id)
                added["@"].append(word[1:])
            except:
                pass
    return added


def lista_post(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT id FROM post')
        res = cursor.fetchall()
        posts = tuple(x[0] for x in res)
        return posts


def acha_post(conn, titulo, email):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM post WHERE titulo=%s AND email=%s", (titulo, email))
        res = cursor.fetchone()
        if res:
            return res
        else:
            return None


def post_esta_ativo(conn, titulo, email):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM post WHERE titulo=%s AND email=%s", (titulo, email))
        res = cursor.fetchone()
        if res:
            return res[4]
        else:
            return None


def acha_post_id(conn, titulo, email):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id FROM post WHERE titulo=%s AND email=%s", (titulo, email))
        res = cursor.fetchone()
        if res:
            return res[0]
        else:
            return None


def adiciona_post(conn, titulo, texto, url, email):
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO post (titulo, texto, url, email)\
                 VALUES (%s, %s, %s, %s)', (titulo, texto, url, email))
        cursor.execute('SELECT id FROM post WHERE id=LAST_INSERT_ID() LIMIT 1')
        id_post = cursor.fetchone()
        return parser_texto(conn, texto, id_post)


def remove_post(conn, titulo, email):
    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE post SET ativo = 0 WHERE titulo=%s AND email=%s", (titulo, email))


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
        cursor.execute(
            'INSERT INTO tag_usuario (email, id) VALUES (%s, %s)', (email, id))


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
        cursor.execute('INSERT INTO tag_passaro (nome, id)\
                 VALUES (%s, %s)', (nome, id))

#Posts do usuário em ordem cronológica reversa
def lista_posts_novos(conn,email):
    with conn.cursor() as cursor:
        cursor.execute('SELECT titulo, texto, url FROM post WHERE email=%s ORDER BY data_post DESC',(email))
        res = cursor.fetchall()
        if res:
            return res
        else:
            return None

#Tabela cruzada de quantidade de aparelhos por tipo e por browser
def x_tbl_dvc_brwsr(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT browser, so, COUNT(so) total FROM usuario_viu GROUP BY browser, so')
        res = cursor.fetchall()
        if res:
            return (res)
        else:
            return None