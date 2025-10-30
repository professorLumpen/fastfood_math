from pydantic import BaseModel


class FibonacciNumber(BaseModel):
    number: int
