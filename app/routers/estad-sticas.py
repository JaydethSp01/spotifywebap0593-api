from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Estadistica(BaseModel):
    id: int
    descripcion: str

estadisticas_db = [
    Estadistica(id=1, descripcion="Estadistica Uno"),
    Estadistica(id=2, descripcion="Estadistica Dos"),
]

@router.get("/estadisticas", response_model=List[Estadistica])
async def get_estadisticas():
    return estadisticas_db

@router.get("/estadisticas/{estadistica_id}", response_model=Estadistica)
async def get_estadistica(estadistica_id: int):
    for estadistica in estadisticas_db:
        if estadistica.id == estadistica_id:
            return estadistica
    raise HTTPException(status_code=404, detail="Estadistica not found")

@router.post("/estadisticas", response_model=Estadistica)
async def create_estadistica(estadistica: Estadistica):
    estadisticas_db.append(estadistica)
    return estadistica

@router.put("/estadisticas/{estadistica_id}", response_model=Estadistica)
async def update_estadistica(estadistica_id: int, estadistica: Estadistica):
    for i, e in enumerate(estadisticas_db):
        if e.id == estadistica_id:
            estadisticas_db[i] = estadistica
            return estadistica
    raise HTTPException(status_code=404, detail="Estadistica not found")

@router.delete("/estadisticas/{estadistica_id}")
async def delete_estadistica(estadistica_id: int):
    for i, estadistica in enumerate(estadisticas_db):
        if estadistica.id == estadistica_id:
            del estadisticas_db[i]
            return {"message": "Estadistica deleted"}
    raise HTTPException(status_code=404, detail="Estadistica not found")
