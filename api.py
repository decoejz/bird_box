from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response
from projeto import *
import json

class Usuario(BaseModel):
    nome: str
    email: str
    cidade: str

class Post(BaseModel):
    nome: str
    email: str
    cidade: str

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


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/usuario")
async def cria_usuario(usuario: Usuario, response: Response):
    with conn.cursor() as cursor:
        cursor.execute('START TRANSACTION')
    try:
        adiciona_usuario(conn, usuario.nome, usuario.email, usuario.cidade)
        with conn.cursor() as cursor:
            cursor.execute('COMMIT')
    except pymysql.err.IntegrityError as e:
        print(e)
        with conn.cursor() as cursor:
            cursor.execute('ROLLBACK')
        response.status_code = 400
        return "algum erro aconteceu", "{}".format(e)
    
    return 200, usuario


@app.post("/post")
async def add_post(post: Post, response: Response):
    return post


@app.delete("/post")
async def rm_post(post: Post, response: Response):
    return "isso"

@app.get("/post/{usuario}")
async def pega_posts_de_usuario(response: Response):
    return "posts"

@app.get("/usuario/populares")
async def pega_usuarios_populares(response: Response):
    return "posts"

@app.get("/usuario/{usuario}/tags")
async def pega_mencoes_ao_usuario(response: Response):
    return "tags"

@app.get("/stats")
async def pega_estatisticas(response: Response):
    return "tags"   

@app.get("/passaro/imagens")
async def pega_imagem_por_passaro(response: Response):
    return "dad"    