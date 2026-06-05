from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Album(BaseModel):
    id: int
    titulo: str

albums_db = [
    Album(id=1, titulo="Album Uno"),
    Album(id=2, titulo="Album Dos"),
]

@router.get("/albums", response_model=List[Album])
async def get_albums():
    return albums_db

@router.get("/albums/{album_id}", response_model=Album)
async def get_album(album_id: int):
    for album in albums_db:
        if album.id == album_id:
            return album
    raise HTTPException(status_code=404, detail="Album not found")

@router.post("/albums", response_model=Album)
async def create_album(album: Album):
    albums_db.append(album)
    return album

@router.put("/albums/{album_id}", response_model=Album)
async def update_album(album_id: int, album: Album):
    for i, a in enumerate(albums_db):
        if a.id == album_id:
            albums_db[i] = album
            return album
    raise HTTPException(status_code=404, detail="Album not found")

@router.delete("/albums/{album_id}")
async def delete_album(album_id: int):
    for i, album in enumerate(albums_db):
        if album.id == album_id:
            del albums_db[i]
            return {"message": "Album deleted"}
    raise HTTPException(status_code=404, detail="Album not found")
