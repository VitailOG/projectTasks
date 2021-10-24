from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from core.db import Base


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    text = Column(String)
    column = Column(Integer, ForeignKey('column.id'))
    column_id = relationship("ColumnTask")


class ColumnTask(Base):
    __tablename__ = "column"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    project = Column(Integer, ForeignKey('project.id'))
    project_id = relationship("Project")
    tasks = relationship("Task", backref="column_id", passive_deletes=True)


task = Task.__table__
column_task = ColumnTask.__table__
