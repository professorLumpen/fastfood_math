from pydantic import BaseModel


class FibonacciNumber(BaseModel):
    number: int


class FibonacciOutput(BaseModel):
    order_id: str
    message: str
