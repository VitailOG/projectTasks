from typing import List

from pydantic import BaseModel
from app.auth import schemas


class AbstractProject(BaseModel):
    title: str


class ListUserProject(AbstractProject):
    id: int


class CreateProject(AbstractProject):
    pass
