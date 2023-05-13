from fastapi import FastAPI
from models.user_connection import UserConnection

app= FastAPI()
conn = UserConnection()

@app.get("/favicon.ico")
async def favicon():
    return {"data": None}

@app.get("/images/icons/{icon_name}")
async def icons(icon_name: str):
    return {"data": None}

@app.get("/")
def root():
    conn
    return "hi, hola que tal"  