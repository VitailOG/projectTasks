from core.db import database
from .services import ProjectService

def get_project_service():
    return ProjectService(database)
