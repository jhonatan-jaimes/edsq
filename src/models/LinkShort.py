from typing import ClassVar

from pydantic import BaseModel


class LinkShort(BaseModel):
    link: str
    cli: str
