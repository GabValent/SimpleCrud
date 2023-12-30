from redis_om import HashModel
from redis_connection import redis_connection
from redis_om import get_redis_connection



class Produto(HashModel):
    name: str
    description: str
    class Meta:
        database: get_redis_connection(host= 'localhost', port='6379')
    











