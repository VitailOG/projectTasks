from typing import List

from pydantic import BaseModel


class CreateOrUpdateTask(BaseModel):
    text: str


class Task(BaseModel):
    id: int
    text: str


class AbstractColumn(BaseModel):
    title: str


class CreateOrUpdateColumn(AbstractColumn):
    pass


class Columns(AbstractColumn):
    id: int
    tasks: List[Task]
