from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Usuario(BaseModel):
    id: int
    nombre: str

usuarios_db = [
    Usuario(id=1, nombre="Juan Perez"),
    Usuario(id=2, nombre="Maria Lopez"),
]

@router.get("/usuarios", response_model=List[Usuario])
async def get_usuarios():
    return usuarios_db

@router.get("/usuarios/{usuario_id}", response_model=Usuario)
async def get_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario not found")

@router.post("/usuarios", response_model=Usuario)
async def create_usuario(usuario: Usuario):
    usuarios_db.append(usuario)
    return usuario

@router.put("/usuarios/{usuario_id}", response_model=Usuario)
async def update_usuario(usuario_id: int, usuario: Usuario):
    for i, u in enumerate(usuarios_db):
        if u.id == usuario_id:
            usuarios_db[i] = usuario
            return usuario
    raise HTTPException(status_code=404, detail="Usuario not found")

@router.delete("/usuarios/{usuario_id}")
async def delete_usuario(usuario_id: int):
    for i, usuario in enumerate(usuarios_db):
        if usuario.id == usuario_id:
            del usuarios_db[i]
            return {"message": "Usuario deleted"}
    raise HTTPException(status_code=404, detail="Usuario not found")
