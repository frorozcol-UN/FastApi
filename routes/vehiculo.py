from fastapi import APIRouter, HTTPException, exceptions
from config.db import conn
from models.index import vehiculos
from schemas.index import Vehiculo

VehiculoAPI = APIRouter()

@VehiculoAPI.get("/")
async def read_all_data():
    return conn.execute(vehiculos.select()).fetchall()

@VehiculoAPI.get("/{id}")
async def read__data(id:int):
    valor = conn.execute(vehiculos.select().where(vehiculos.c.id == id)).fetchall()
    if valor:
        return valor
    else:
        return HTTPException(status_code=404, detail="item no encotrado")
        

@VehiculoAPI.post("/")
async def write_data(vehiculo:Vehiculo):
        conn.execute(vehiculos.insert().values(
            placa=vehiculo.placa,
            celda=vehiculo.celda
        ))
        return conn.execute(vehiculos.select()).fetchall()

@VehiculoAPI.put("/{id}")
async def update_data(id:int, vehiculo:Vehiculo):

        values =conn.execute(vehiculos.update().values(
            placa=vehiculo.placa,
            celda=vehiculo.celda
        ))
        values = conn.execute(vehiculos.select().where(vehiculos.c.id == id)).fetchall()
        if values:
            return values
        else:
            return HTTPException(status_code=404, detail="item no encotrado")


@VehiculoAPI.delete("/{id}")
async def remove_vehiculo(id:int):
    conn.execute(vehiculos.delete().where(vehiculos.c.id==id))
    return conn.execute(vehiculos.select()).fetchall()