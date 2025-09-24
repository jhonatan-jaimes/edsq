from fastapi import APIRouter
from src.models import Message

routes = APIRouter(prefix="/api", tags=["decode"])


@routes.post("/decode")
async def decode(text: Message):
    return None
