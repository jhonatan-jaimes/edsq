from src.application import routes
from src.models import Message


@routes.post("/encode")
async def encode(text: Message):
    pass
