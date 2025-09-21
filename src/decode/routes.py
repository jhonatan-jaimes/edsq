from fastapi import APIRouter
from src.models import Message

routes = APIRouter(prefix="/api")

@routes.post("/decode")
async def decode(text: Message):
    return None
