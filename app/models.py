from pydantic import BaseModel
from typing import Optional

class InventoryItem(BaseModel):
    id: int
    name: str
    category: str
    quantity: int
    photo_path: Optional[str] = None
    needed: bool = False
