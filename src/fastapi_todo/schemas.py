"""Pydantic-модели для сериализации данных."""

from pydantic import BaseModel


class TodoCreate(BaseModel):
    """Входная модель: что передаёт клиент при создании задачи."""

    title: str


class Todo(BaseModel):
    """Выходная модель: данные задачи в ответе API."""

    id: int
    title: str
    done: bool = False