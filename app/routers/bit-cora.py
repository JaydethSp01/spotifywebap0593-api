from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Bitacora(BaseModel):
    id: int
    titulo: str

bitacoras_db = [
    Bitacora(id=1, titulo="Bitacora Uno"),
    Bitacora(id=2, titulo="Bitacora Dos"),
]

@router.get("/bitacoras", response_model=List[Bitacora])
async def get_bitacoras():
    return bitacoras_db

@router.get("/bitacoras/{bitacora_id}", response_model=Bitacora)
async def get_bitacora(bitacora_id: int):
    for bitacora in bitacoras_db:
        if bitacora.id == bitacora_id:
            return bitacora
    raise HTTPException(status_code=404, detail="Bitacora not found")

@router.post("/bitacoras", response_model=Bitacora)
async def create_bitacora(bitacora: Bitacora):
    bitacoras_db.append(bitacora)
    return bitacora

@router.put("/bitacoras/{bitacora_id}", response_model=Bitacora)
async def update_bitacora(bitacora_id: int, bitacora: Bitacora):
    for i, b in enumerate(bitacoras_db):
        if b.id == bitacora_id:
            bitacoras_db[i] = bitacora
            return bitacora
    raise HTTPException(status_code=404, detail="Bitacora not found")

@router.delete("/bitacoras/{bitacora_id}")
async def delete_bitacora(bitacora_id: int):
    for i, bitacora in enumerate(bitacoras_db):
        if bitacora.id == bitacora_id:
            del bitacoras_db[i]
            return {"message": "Bitacora deleted"}
    raise HTTPException(status_code=404, detail="Bitacora not found")
