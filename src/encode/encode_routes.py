from src.application import routes
from src.models import Message


@routes.post("/encode")
async def encode(text_to_encode: Message):
    text_array = list(text_to_encode.text)
    pass
