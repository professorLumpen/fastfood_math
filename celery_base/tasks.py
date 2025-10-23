from fastapi import HTTPException, status

from celery_base.celery_app import celery_app


@celery_app.task
def very_slow_calculate_fibonacci(number: int) -> int:
    if number < 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "value must be positive")

    if number <= 1:
        return number

    return very_slow_calculate_fibonacci(number - 1) + very_slow_calculate_fibonacci(number - 2)
