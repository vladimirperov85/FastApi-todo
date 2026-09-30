"""Пакет fastapi_todo — точка входа приложения."""

from fastapi import FastAPI

from .router import router

def create_app() -> FastAPI:
    """Фабрика приложения: собирает FastAPI и подключает маршруты."""
    app = FastAPI(
        title="FastAPI Todo",
        version="0.1.0",
        description="Минимальный CRUD «список задач» (in-memory).",
    )

    @app.get("/", tags=["service"])
    def healthcheck() -> dict[str, str]:
        """Эндпоинт-«живость»: подтверждает, что приложение поднялось."""
        return {"status": "ok"}
    
    app.include_router(router)

    return app


app = create_app()