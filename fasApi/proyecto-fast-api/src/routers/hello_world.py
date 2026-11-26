# app/routers/paso1_bienvenida.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


@router.get("/")
def bienvenida() -> dict[str, str]:
    return {"mensaje": "Bienvenido al curso de FastAPI + uv", "paso": "1"}

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str

@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv",
            "autor": "Antoni Fernandez",
            "version": "1.0.0"
            }

@router.get("/antoni")
def endpoint_a() -> Mensaje:
    return Mensaje(texto="Hola Antoni", campo_interno="desde antoni link")

@router.get("/fernandez", response_model=Mensaje)
def endpoint_b():
    return {"texto": "Hola Antoni Fernandez",
            "prioridad": 5,
            "campo_interno": "imprime desde endpoint antoni link"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra(): 
    return {"texto": "Hola Antoni",
            "prioridad": 5,
            "campo_interno": "si debe salir incluido en el modelo",
            "campo_extra": "no deberia salir"
            }


