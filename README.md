# FastAPI Todo

Минимальный CRUD-сервис «список задач» на FastAPI. Хранилище — в памяти (in-memory).

## Запуск

```bash
uv run uvicorn fastapi_todo:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

## Эндпоинты

| Метод | Путь | Описание |
|---|---|---|
| GET | `/` | Healthcheck |
| GET | `/todos` | Список задач |
| POST | `/todos` | Создать задачу (201) |
| GET | `/todos/{id}` | Получить задачу по id (404 если нет) |
| PUT | `/todos/{id}` | Обновить задачу |
| DELETE | `/todos/{id}` | Удалить задачу (204) |

## Примеры

```bash
# Создать задачу
curl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"buy bread"}'

# Получить список
curl http://127.0.0.1:8000/todos

# Обновить
curl -X PUT http://127.0.0.1:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"updated task"}'

# Удалить
curl -X DELETE http://127.0.0.1:8000/todos/1
```
