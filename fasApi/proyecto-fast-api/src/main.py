from fastapi import FastAPI
from routers.hello_world import router
from routers.task_router import tasks_router

app = FastAPI(title="Curso FastAPI + uv")

app.include_router(router)
app.include_router(tasks_router)