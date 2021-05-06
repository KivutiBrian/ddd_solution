from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime

class AttendantBase(BaseModel):
    FirstName: str
    LastName: str
    EmailAddress: str
    PrimaryNumber: str

class AttendantPost(AttendantBase):
    Password: str

class Attendant(AttendantBase):
    Id: str
    PublicId: str

    class Config:
        orm_mode = True