from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime


# Id = Column(Integer, primary_key=True)
# PublicId = Column(String, nullable=False)
# Title = Column(String, nullable=False)
# Description = Column(Text, nullable=False)
# CreatedAt = Column(DateTime, nullable=False, default=func.now())
# UpdatedAt = Column(DateTime, nullable=False, default=func.now())

class RoleBase(BaseModel):
    Title: str
    Description: str

class Role(RoleBase):
    Id: str
    PublicId: str
    CreatedAt: Optional[datetime]
    UpdatedAt: Optional[datetime]

    class Config:
        orm_mode = True
