from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from app.routers import usuario, album, bitacora, estadisticas, tarjeta_estetica
app = FastAPI()
origins = os.environ.get('CORS_ORIGINS', '*').split(',')
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.include_router(usuario.router)
app.include_router(album.router)
app.include_router(bitacora.router)
app.include_router(estadisticas.router)
app.include_router(tarjeta_estetica.router)
@app.get('/health')
async def health_check():
    return {'status': 'healthy'}
