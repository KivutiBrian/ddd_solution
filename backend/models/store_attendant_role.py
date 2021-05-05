# custom imports
from .base import Model
from configs.config_sqlalchemy import Base

# SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, JSON, Text, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

class StoreAttendantRole(Base, Model):
    __tablename__ = 'store_attendant_role'
    Id = Column(Integer, primary_key=True)
    PublicId = Column(String, nullable=False)
    StoreId = Column(Integer, ForeignKey('stores.Id'), nullable=False)
    UserId = Column(Integer, ForeignKey('attendants.Id'), nullable=False)
    RoleId = Column(Integer, ForeignKey('roles.Id'), nullable=False)
    CreatedAt = Column(DateTime, nullable=False, default=func.now())
    UpdatedAt = Column(DateTime, nullable=False, default=func.now())

    store = relationship('StoreModel', back_populates='attendants')
    attendant = relationship('AttendantModel', back_populates='stores')