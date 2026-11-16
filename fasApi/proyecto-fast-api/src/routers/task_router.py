from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

tasks_router = APIRouter(tags=["Tasks"])


# --- MODELOS PYDANTIC (Patrón Create / Read / Update) ---
class TaskCreate(BaseModel):
    title: str = Field(
        min_length=3, max_length=100, description="Título de la tarea"
    )
    description: str | None = Field(default=None, max_length=500)
    priority: str = Field(
        default="medium", description="'low', 'medium' o 'high'"
    )
    tags: list[str] = Field(default_factory=list)


class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    priority: str
    tags: list[str]
    is_completed: bool


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    description: str | None = None
    priority: str | None = None
    tags: list[str] | None = None
    is_completed: bool | None = None


# --- BASE DE DATOS EN MEMORIA ---
TASKS: list[dict] = []
NEXT_ID = 1


# --- ENDPOINTS ---


# 1. CREATE (POST)
@tasks_router.post(
    "/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED
)
def create_task(task: TaskCreate) -> dict:
    global NEXT_ID
    new_task = {
        "id": NEXT_ID,
        "is_completed": False,
        "internal_notes": (  # Campo interno oculto gracias a response_model=TaskRead
            "creado desde la API"
        ),
        **task.model_dump(),
    }
    TASKS.append(new_task)
    NEXT_ID += 1
    return new_task


# 2. READ ALL (GET)
@tasks_router.get("/tasks", response_model=list[TaskRead])
def list_tasks() -> list[dict]:
    return TASKS


# 3. READ ONE (GET por ID)
@tasks_router.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int) -> dict:
    for task in TASKS:
        if task["id"] == task_id:
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada"
    )


# 4. UPDATE PARTIAL (PATCH)
@tasks_router.patch("/tasks/{task_id}", response_model=TaskRead)
def update_task(task_id: int, update: TaskUpdate) -> dict:
    for task in TASKS:
        if task["id"] == task_id:
            changes = update.model_dump(exclude_unset=True)
            task.update(changes)
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada"
    )


# 5. DELETE
@tasks_router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    for index, task in enumerate(TASKS):
        if task["id"] == task_id:
            TASKS.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada"
    )