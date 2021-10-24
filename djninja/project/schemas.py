from typing import List
from ninja import Schema


class AbstractSchema(Schema):
    title: str


class CreateOrUpdateProject(AbstractSchema):
    pass


class Projects(AbstractSchema):
    id: int


class AbstractTaskSchema(Schema):
    text: str


class Tasks(AbstractTaskSchema):
    id: int


class CreateOrUpdateTask(AbstractTaskSchema):
    pass


class AuthLogin(Schema):
    username: str
    password: str



class Columns(AbstractSchema):
    id: int
    tasks: List[Tasks] = []


class CreateOrUpdateColumn(AbstractSchema):
    pass
