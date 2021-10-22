from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    admin = Column(Integer, ForeignKey('users.id'))
    admin_id = relationship("User")


project = Project.__table__
