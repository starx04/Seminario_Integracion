# API de la tienda de equipos móviles

Proyecto educativo basado en la estructura FastAPI del repositorio. Expone un
catálogo de celulares con operaciones para consultar, agregar, actualizar y
eliminar equipos. Los datos se mantienen en memoria y se reinician al detener
la aplicación.

## Ejecutar

Desde esta carpeta, instala las dependencias y levanta el servidor:

```bash
uv sync
uv run fastapi dev src/tienda_equipos_moviles/main.py
```

La documentación interactiva queda disponible en `http://127.0.0.1:8000/docs`.

## Rutas

- `GET /`: bienvenida y enlace al catálogo.
- `GET /equipos`: listar equipos.
- `GET /equipos/{id}`: consultar un equipo.
- `POST /equipos`: agregar un equipo.
- `PUT /equipos/{id}`: actualizar un equipo.
- `DELETE /equipos/{id}`: eliminar un equipo.
