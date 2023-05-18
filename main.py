from fastapi import FastAPI
from models.user_connection import UserConnection
from schema.user_schema import UserSchema

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
    items=[]
    for data in conn.read_all():
        print(data)


@app.post("/api/insert")
def insert(user_data:UserSchema):
    data = user_data.dict()
    data.pop("id")
    conn.write(data)