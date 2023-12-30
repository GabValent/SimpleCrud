from fastapi import FastAPI
from routerarq import router


 
app = FastAPI()

@app.get('/')
async def Home():
    return "Seja Bem vindo"

app.include_router(router)


