from fastapi import APIRouter
from src.models import LinkShort, Message
from .Service import Service


service = Service()
routes = APIRouter(prefix="/api", tags=["short"])


@routes.post("/short")
async def short_url(links: LinkShort):
    return Message(text=service.create_save_link(links))
