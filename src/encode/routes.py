from fastapi import APIRouter
from src.models import Message
from .Service import Service

routes = APIRouter(prefix="/api")
service = Service()


@routes.post("/encode")
async def encode(text_to_encode: Message):
    return Message(text=service.encode_text(text_to_encode))
