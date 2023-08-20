import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def dar_bom_dia():
    return {"resposta":"bom dia"}