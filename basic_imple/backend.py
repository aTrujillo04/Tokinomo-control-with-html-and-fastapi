from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 1. Configuración de CORS
# Esto es vital: permite que tu frontend (que puede correr en un puerto)
# hable con tu API (que corre en otro puerto).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite peticiones desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

# 2. Modelo de datos
# Definimos qué esperamos recibir del HTML (un JSON con un campo "nombre")
class Usuario(BaseModel):
    nombre: str 

# 3. Endpoint
# Recibe datos (POST) y devuelve datos (return)
@app.post("/saludar")
def procesar_saludo(usuario: Usuario):

    if not usuario.nombre or usuario.nombre.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="El nombre no puede estar vacío. status code=400"
        )

    mensaje_respuesta = (
        f"¡Hola {usuario.nombre}! Este es un mensaje de respuesta desde el backend, status code=200"
    )
    return {"respuesta": mensaje_respuesta}

@app.post("/despedir")
def procesar_despedida(usuario:Usuario):

    if not usuario.nombre or usuario.nombre.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="El nombre no puede estar vacío. status code=400"
        )

    mensaje_respuesta = (
        f"¡Hola {usuario.nombre}! Este es un mensaje de despedida desde el backend, status code=200"
    )
    return {"respuesta": mensaje_respuesta}

    
