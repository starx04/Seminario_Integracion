# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from routers.hello_world import router

app = FastAPI(title="Curso FastAPI + uv")

app.include_router(router)
