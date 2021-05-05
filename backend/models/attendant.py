# custom imports
from .base import Model
from configs.config_sqlalchemy import Base

# SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, JSON, Text, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

class AttendantModel(Base, Model):
    __tablename__ = 'attendants'
    Id = Column(Integer, primary_key=True)
    PublicId = Column(String, nullable=False)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    EmailAddress = Column(String, nullable=False)
    PrimaryNumber = Column(String, nullable=False)
    IsActive = Column(Boolean, default=True, nullable=False)
    CreatedAt = Column(DateTime, nullable=False, default=func.now())
    UpdatedAt = Column(DateTime, nullable=False, default=func.now())

    stores = relationship('StoreAttendantRole', back_populates='attendant', cascade="all, delete, delete-orphan")
