from fastapi import FastAPI

from tienda_equipos_moviles.routers.equipos import router as equipos_router

app = FastAPI(
    title="Tienda de Equipos Móviles",
    description="API educativa para administrar el catálogo de celulares.",
    version="1.0.0",
)


@app.get("/")
def bienvenida() -> dict[str, str]:
    return {
        "mensaje": "Bienvenido a la API de la tienda de equipos móviles",
        "catalogo": "/equipos",
        "documentacion": "/docs",
    }


app.include_router(equipos_router)
