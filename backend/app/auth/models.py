from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=False)


user = User.__table__
