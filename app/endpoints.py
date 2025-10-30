from fastapi import APIRouter, Depends

from app.schemas import FibonacciNumber, FibonacciCreated, FibonacciGetOrder, FibonacciResult
from celery_base.celery_service import TaskService, get_task_service
from celery_base.tasks import very_slow_calculate_fibonacci


fibonacci_router = APIRouter(prefix="/fibonacci", tags=["fibonacci"])


@fibonacci_router.get(
    "/",
    response_model=FibonacciResult,
)
async def get_fibonacci_result(
    order_info: FibonacciGetOrder,
    task_service: TaskService = Depends(get_task_service),
):
    status, result = task_service.fetch_result(order_info.order_id)

    response = {
        "order_status": status,
        "result": result,
    }

    return response


@fibonacci_router.post(
    "/",
    response_model=FibonacciCreated,
)
async def calculate_fibonacci_number(
        fib: FibonacciNumber,
        task_service: TaskService = Depends(get_task_service)
):
    number = fib.number
    result = task_service.create_task(
        task=very_slow_calculate_fibonacci,
        number=number,
    )

    response = {
        "order_id": result.id,
        "message": "Use the order ID in the GET request to get the result"
    }

    return response
