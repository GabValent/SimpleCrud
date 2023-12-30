from fastapi import APIRouter
from schema import Produto
from redis_connection import redis_connection


redis = redis_connection().connect() 
router = APIRouter()

def format_produto(produto: Produto):
    return {
        "name": produto.name,
        "description": produto.description
    }

@router.post("/produto")
async def create(produto: Produto):
    redis.hmset(produto.pk,format_produto(produto))
    
    
    return "Produto inserido com sucesso"


@router.get("/produtos")
async def busca():
    redis_keys = redis.keys()
    dict = {}
    for key in redis_keys:
        product_name = redis.hget(key, "name")
        dict[key.decode("utf-8")] = product_name.decode("utf-8")
    return dict

    

@router.put("/produto/{pk}")
async def update(pk:str, produto:Produto):
    produto_procurado = redis.hgetall(pk)
    produto_procurado["name"] = produto.name
    produto_procurado["description"] = produto.description
    redis.hmset(pk,produto_procurado)
    
    return "Alterado com sucesso"



@router.delete("/produto/{pk}")
async def delete(pk:str):
    redis.delete(pk)
    
    return "Deletado com sucesso"








