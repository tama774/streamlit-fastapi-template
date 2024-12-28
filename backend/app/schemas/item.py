from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    name: str = Field(..., title="Item Name", max_length=100)
    description: str = Field(..., title="Item Description", max_length=500)

class ItemResponse(ItemBase):
    id: int

class ItemListResponse(BaseModel):
    items: dict[int, ItemResponse]

class CreateItemRequest(ItemBase):
    pass
