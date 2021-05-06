from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime

class StoreBase(BaseModel):
    StoreName: str
    OwnerFirstName: str
    OwnerLastName: str
    OwnerEmail: str

class Store(StoreBase):
    Id: int
    PublicId: str
    CreatedAt: Optional[datetime]
    UpdatedAt: Optional[datetime]

    class Config:
        orm_mode = True

    