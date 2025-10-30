from pydantic import BaseModel


class FibonacciNumber(BaseModel):
    number: int


class FibonacciCreated(BaseModel):
    order_id: str
    message: str


class FibonacciGetOrder(BaseModel):
    order_id: str


class FibonacciResult(BaseModel):
    order_status: str
    result: str | None = None