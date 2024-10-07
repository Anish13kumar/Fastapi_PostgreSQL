from .database import Base

from sqlalchemy import Column,String,Integer,UUID
import uuid

class Users(Base):
    __tablename__ = "super_admins"
    id = Column(UUID(36), primary_key=True, default=uuid.uuid4()) 
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)