from typing import Union
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

User = "Via003"
PWD = "Viasat3"

class Satellite(BaseModel):
    name: str
    coordinates: float
    longitude: str
    status: str

class Credentials(BaseModel):
    user: str
    pwd: str

class Message(BaseModel):
    text:str

@app.post("/login")
def login(credentials: Credentials):
    if credentials.user == User and credentials.pwd == PWD:
        return {"message": "Bienvenido al Control de Mision de Viasat"}
    else:
        return {"message": "Intenta de nuevo"}

@app.get("/satellites")
def get_satellites():
    satellites = [
        Satellite(name="AnikF F2", coordinates=111.1, longitude="Oeste", status="Saludable, Sin Detalles"),
        Satellite(name="Wildblue 1", coordinates=111.1, longitude="Oeste", status="Saludable, Sin Detalles"),
        Satellite(name="Viasat 1", coordinates=115.1, longitude="Oeste", status="Saludable, Sin Detalles"),
        Satellite(name="Viasat 2", coordinates=69.9, longitude="Oeste", status="Saludable, Sin Detalles"),
        Satellite(name="Viasat 3", coordinates=89.9, longitude="Oeste", status="Requiere Actualizacion")
    ]
    return satellites

@app.get("/antenna")
def verify_antenna():
    point = [Message(text="Punteo Correcto, Antenas de Central Terrestre apuntadas a los Satelites, Sistemas en Linea")]
    return point
@app.get("/update")
def update_os():
    os = [
        Message(text="Actualizacion correcta, Sistemas en Linea"),
        Message(text="Sistema Orbital Activado")
    ]
    return os
@app.get("/saymtex")
def input_text():
    osi = [
        Message(text="Bienvenido al Control de Mision de Viasat")
    ]
    usern = input("Usuario: ")
    pwds = input("clave: ")
    return osi 
    


if __name__ == '__main__':
    uvicorn.run(app,port=8000,host="0.0.0.0")
