from typing import Any

from celery.result import AsyncResult

from celery_base.celery_app import celery_app


class TaskService:
    def __init__(self, celery_app):
        self.app = celery_app

    def create_task(
            self,
            task: callable,
            *args,
            **kwargs,
    ) -> AsyncResult:
        result = task.delay(*args, **kwargs)
        return result

    def fetch_result(
            self,
            id: str,
    ) -> tuple[str, Any]:
        result = AsyncResult(
            id=id,
            app=self.app,
        )

        if result.ready():
            return result.status, result.get()

        return result.status, None


async def get_task_service():
    yield TaskService(celery_app)
