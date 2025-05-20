# models.py
from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str = Field(...)
    description: Optional[str] = None
    price: float

class ItemUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
