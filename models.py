from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id                  = Column(Integer, primary_key=True, index=True)
    name                = Column(String, index=True)
    lastname            = Column(String, index=True)
    email               = Column(String, index=True, unique=True)
    hashed_password     = Column(String, index=True)


