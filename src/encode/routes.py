from fastapi import APIRouter
from src.models import Message
from .Service import Service

routes = APIRouter(prefix="/api")
service = Service()

@routes.post("/encode")
async def encode(text_to_encode: Message):
    encode = service.encode_text(text_to_encode)
    texto_final = ""
    for i in encode:
        texto_final += i
    return Message(text= texto_final)
