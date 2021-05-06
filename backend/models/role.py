from .base import Model
from configs.config_sqlalchemy import Base

# SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime,BIGINT, JSON, Text, Float, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy import func

class RoleModel(Base, Model):
    __tablename__ = 'roles'
    Id = Column(Integer, primary_key=True)
    PublicId = Column(String, nullable=False)
    Title = Column(String, nullable=False)
    Description = Column(Text, nullable=False)
    CreatedAt = Column(DateTime, nullable=False, default=func.now())
    UpdatedAt = Column(DateTime, nullable=False, default=func.now())
    
    users = relationship('StoreAttendantRole', backref='role', cascade="all, delete, delete-orphan")

    @classmethod
    def check_role_exists(cls):
        