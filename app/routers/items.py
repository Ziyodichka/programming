from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/items", tags=["items"])

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# In-memory "database"
fake_db: List[Item] = [
    Item(id=1, name="Noutbuk", description="Gaming noutbuk", price=1200.0),
    Item(id=2, name="Telefon", description="Smartfon", price=800.0),
    Item(id=3, name="Quloqchin", description="Simsiz quloqchin", price=150.0),
]

@router.get("/", response_model=List[Item])
def get_items():
    return fake_db

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = next((i for i in fake_db if i.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item topilmadi")
    return item

@router.post("/", response_model=Item, status_code=201)
def create_item(item: Item):
    fake_db.append(item)
    return item
