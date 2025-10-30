from pydantic import BaseModel, Field


class FibonacciNumber(BaseModel):
    number: int = Field(..., ge=1)


class FibonacciCreated(BaseModel):
    order_id: str
    message: str


class FibonacciResult(BaseModel):
    order_status: str
    result: int | None = None
