from pydantic import BaseModel, condecimal, constr, Field
from typing import Optional

class ProductCreate(BaseModel):
    name: constr(min_length=1, max_length=255)
    description: Optional[str] = None
    quantity: int = Field(ge=0)
    price: condecimal(gt=0, decimal_places=2)

class ProductRead(BaseModel):
    id: int
    name: str
    description: Optional[str]
    quantity: int
    price: condecimal(max_digits=10, decimal_places=2)
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True
