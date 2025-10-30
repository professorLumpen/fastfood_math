from fastapi import FastAPI

from app.endpoints import fibonacci_router


app = FastAPI()

app.include_router(fibonacci_router)
