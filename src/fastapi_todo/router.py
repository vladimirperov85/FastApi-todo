"""Маршруты API для задач."""

from fastapi import APIRouter, HTTPException

from .schemas import Todo, TodoCreate
from .store import TodoStore

router = APIRouter()

# Общий экземпляр хранилища для всех запросов
_store = TodoStore()


@router.get("/todos", response_model=list[Todo], tags=["todos"])
def list_todos() -> list[Todo]:
    """Возвращает все задачи."""
    return _store.list_all()


@router.post("/todos", response_model=Todo, status_code=201, tags=["todos"])
def create_todo(todo: TodoCreate) -> Todo:
    """Создаёт новую задачу."""
    return _store.create(title=todo.title)

@router.get("/todos/{todo_id}", response_model=Todo, tags=["todos"])
def get_todo(todo_id: int) -> Todo:
    """Возвращает задачу по id или 404."""
    todo = _store.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return todo


@router.put("/todos/{todo_id}", response_model=Todo, tags=["todos"])
def update_todo(todo_id: int, todo_update: TodoCreate) -> Todo:
    """Обновляет задачу по id."""
    updated = _store.update(todo_id, title=todo_update.title)
    if updated is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/todos/{todo_id}", status_code=204, tags=["todos"])
def delete_todo(todo_id: int) -> None:
    """Удаляет задачу по id."""
    deleted = _store.delete(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")