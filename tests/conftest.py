"""Фикстуры для тестов."""

import pytest
from fastapi.testclient import TestClient

from fastapi_todo import create_app
from fastapi_todo.router import _store


@pytest.fixture
def client():
    """Каждый тест получает TestClient с пустым хранилищем."""
    _store._store.clear()
    _store._next_id = 1
    with TestClient(create_app()) as client:
        yield client