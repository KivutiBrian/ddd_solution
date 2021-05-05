# custom imports
from .base import Model
from configs.config_sqlalchemy import Base

# SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, JSON, Text, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

class StoreModel(Base, Model):
    __tablename__ = 'stores'
    Id = Column(Integer, primary_key=True)
    PublicId = Column(String, nullable=False)
    StoreName = Column(String, nullable=False)
    OwnerFirstName = Column(String, nullable=False)
    OwnerLastName = Column(String, nullable=False)
    OwnerEmail = Column(String, nullable=False)
    CreatedAt = Column(DateTime, nullable=False, default=func.now())
    UpdatedAt = Column(DateTime, nullable=False, default=func.now())

    attendants = relationship('StoreAttendantRole', back_populates='store', cascade="all, delete, delete-orphan")



    
    