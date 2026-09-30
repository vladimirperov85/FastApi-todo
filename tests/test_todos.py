"""Тесты CRUD-эндпоинтов."""

from fastapi.testclient import TestClient


def test_healthcheck(client: TestClient):
    """Healthcheck возвращает status ok."""
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_list_empty(client: TestClient):
    """Список задач пуст, если ничего не создавали."""
    resp = client.get("/todos")
    assert resp.status_code == 200
    assert resp.json() == []


def test_create_todo(client: TestClient):
    """Создание задачи возвращает 201 и задачу с id."""
    resp = client.post("/todos", json={"title": "new task"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == "new task"
    assert data["done"] is False
    assert data["id"] == 1


def test_get_todo(client: TestClient):
    """Получение задачи по id."""
    client.post("/todos", json={"title": "get test"})
    resp = client.get("/todos/1")
    assert resp.status_code == 200
    assert resp.json()["title"] == "get test"


def test_get_not_found(client: TestClient):
    """Получение несуществующей задачи — 404."""
    resp = client.get("/todos/999")
    assert resp.status_code == 404


def test_update_todo(client: TestClient):
    """Обновление задачи."""
    client.post("/todos", json={"title": "old"})
    resp = client.put("/todos/1", json={"title": "new"})
    assert resp.status_code == 200
    assert resp.json()["title"] == "new"


def test_delete_todo(client: TestClient):
    """Удаление задачи — 204."""
    client.post("/todos", json={"title": "delete me"})
    resp = client.delete("/todos/1")
    assert resp.status_code == 204


def test_list_after_operations(client: TestClient):
    """Список отражает текущее состояние."""
    client.post("/todos", json={"title": "a"})
    client.post("/todos", json={"title": "b"})
    resp = client.get("/todos")
    assert len(resp.json()) == 2