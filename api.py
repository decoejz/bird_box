from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response
from projeto import *
import json
from functools import partial

def run_query(connection, query, args=None):
    with connection.cursor() as cursor:
        print('Executando query:')
        cursor.execute(query, args)
        for result in cursor:
            print(result)


class Usuario(BaseModel):
    nome: str = None
    email: str
    cidade: str = None

class Post(BaseModel):
    titulo: str
    texto: str = None
    url: str = None
    email: str

def setUp(config):
    print(config)
    return pymysql.connect(
        host=config['HOST'],
        user=config['USER'],
        password=config['PASS'],
        database='bird_box'
    )

with open('config_testes.json') as f:
    config = json.load(f)
conn = setUp(config)

db = partial(run_query, conn)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "BORA COMEÇAR ESSA BAGAÇA"}

@app.post("/usuario")
async def cria_usuario(usuario: Usuario, response: Response):
    db('START TRANSACTION')
    try:
        adiciona_usuario(conn, usuario.nome, usuario.email, usuario.cidade)
        usr = acha_usuario(conn, usuario.nome)
        db('COMMIT')
        return usr
    except pymysql.err.IntegrityError as e:
        print(e)
        db('ROLLBACK')
        response.status_code = 400
        return "algum erro aconteceu", "{}".format(e)
    

@app.post("/post")
async def add_post(post: Post, response: Response):
    db('START TRANSACTION')
    try:
        tags_added = adiciona_post(conn, post.titulo, post.texto, post.url, post.email)
        
        db_post = acha_post(conn, post.titulo, post.email)
        db('COMMIT')
    except pymysql.err.IntegrityError as e:
        print(e)
        db('ROLLBACK')
        response.status_code = 400
        return "Algum erro aconteceu:", "{}".format(e)
    
    return db_post,tags_added


@app.delete("/post")
async def rm_post(post: Post, response: Response):
    db('START TRANSACTION')
    try:    
        remove_post(conn, post.titulo, post.email)
    except pymysql.err.IntegrityError as e:
        print(e)
        db('ROLLBACK')
        response.status_code = 400
    return "sucessfully deleted post \"{}\"".format(post.titulo)


@app.get("/post")
async def pega_posts_de_usuario(usuario ,response: Response):
    try:    
        posts = lista_post_de_usuario(conn, usuario.email)
    except pymysql.err.IntegrityError as e:
        print(e)
    return posts


@app.get("/usuario/populares")
async def pega_usuarios_populares(response: Response):
    try:
        populares = lista_view_populares(conn)
        if(populares):
            return populares
    except pymysql.err.IntegrityError as e:
        print(e)
        return "error: {}".format(e)

@app.get("/usuario/tags")
async def pega_mencoes_ao_usuario(usuario: Usuario,response: Response):
    shouts = acha_shout_ao_usuario(conn, usuario.email)
    if(shouts):
        return shouts
    else:
        return ""

@app.get("/stats")
async def pega_estatisticas(response: Response):
    stat = x_tbl_dvc_brwsr(conn)
    if(stat):
        return stat
    else:
        return ""

@app.get("/passaro/imagens")
async def pega_imagem_por_passaro(response: Response):
    links = pega_passaro_imagens(conn)
    if(links):
        return links
    else:
        return ""