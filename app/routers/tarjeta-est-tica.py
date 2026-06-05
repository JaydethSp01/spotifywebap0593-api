from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class TarjetaEstetica(BaseModel):
    id: int
    nombre: str

esteticas_db = [
    TarjetaEstetica(id=1, nombre="Tarjeta Uno"),
    TarjetaEstetica(id=2, nombre="Tarjeta Dos"),
]

@router.get("/tarjetas", response_model=List[TarjetaEstetica])
async def get_tarjetas():
    return esteticas_db

@router.get("/tarjetas/{tarjeta_id}", response_model=TarjetaEstetica)
async def get_tarjeta(tarjeta_id: int):
    for tarjeta in esteticas_db:
        if tarjeta.id == tarjeta_id:
            return tarjeta
    raise HTTPException(status_code=404, detail="Tarjeta not found")

@router.post("/tarjetas", response_model=TarjetaEstetica)
async def create_tarjeta(tarjeta: TarjetaEstetica):
    esteticas_db.append(tarjeta)
    return tarjeta

@router.put("/tarjetas/{tarjeta_id}", response_model=TarjetaEstetica)
async def update_tarjeta(tarjeta_id: int, tarjeta: TarjetaEstetica):
    for i, t in enumerate(esteticas_db):
        if t.id == tarjeta_id:
            esteticas_db[i] = tarjeta
            return tarjeta
    raise HTTPException(status_code=404, detail="Tarjeta not found")

@router.delete("/tarjetas/{tarjeta_id}")
async def delete_tarjeta(tarjeta_id: int):
    for i, tarjeta in enumerate(esteticas_db):
        if tarjeta.id == tarjeta_id:
            del esteticas_db[i]
            return {"message": "Tarjeta deleted"}
    raise HTTPException(status_code=404, detail="Tarjeta not found")
