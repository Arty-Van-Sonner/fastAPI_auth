from typing import Optional
from pydantic import BaseModel

class TestGet(BaseModel):
    title: str
    body: Optional[str]