from src.application import routes
from src.models import Message


@routes.post("/decode")
async def decode(text: Message):
    return None
