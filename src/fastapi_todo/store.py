"""In-memory хранилище задач."""

from collections import defaultdict
from typing import Optional

from .schemas import Todo


class TodoStore:
    """Хранит задачи в памяти: dict[id, Todo] + автоинкрементный счётчик."""

    def __init__(self) -> None:
        self._store: dict[int, Todo] = {}
        self._next_id: int = 1

    def list_all(self) -> list[Todo]:
        """Возвращает все задачи."""
        return list(self._store.values())

    def get(self, todo_id: int) -> Optional[Todo]:
        """Возвращает задачу по id или None, если не найдена."""
        return self._store.get(todo_id)

    def create(self, title: str) -> Todo:
        """Создаёт задачу, возвращает готовую Todo с присвоенным id."""
        todo = Todo(id=self._next_id, title=title)
        self._store[self._next_id] = todo
        self._next_id += 1
        return todo

    def update(self, todo_id: int, title: Optional[str] = None, done: Optional[bool] = None) -> Optional[Todo]:
        """Обновляет задачу по id. Если не найдена — возвращает None."""
        todo = self._store.get(todo_id)
        if todo is None:
            return None
        if title is not None:
            todo = todo.model_copy(update={"title": title})
            self._store[todo_id] = todo
        if done is not None:
            todo = todo.model_copy(update={"done": done})
            self._store[todo_id] = todo
        return todo

    def delete(self, todo_id: int) -> bool:
        """Удаляет задачу по id. Возвращает True если удалена, False если не найдена."""
        if todo_id in self._store:
            del self._store[todo_id]
            return True
        return False