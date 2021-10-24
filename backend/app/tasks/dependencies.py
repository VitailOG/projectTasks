from core.db import database
from .services.column import ColomnService
from .services.task import TaskService


def get_task_service():
    return TaskService(database=database)


def get_column_service():
    return ColomnService(database=database)
