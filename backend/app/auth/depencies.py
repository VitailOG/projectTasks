
from .services import AuthService
from core.db import database


def get_auth_service():
    return AuthService(database=database)
    
