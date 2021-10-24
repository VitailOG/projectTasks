from pydantic import BaseModel


class AbstractUser(BaseModel):
    email: str
    username: str
    is_active: bool 


class User(AbstractUser):
    id: int


class CreateUser(AbstractUser):
    password: str


class Token(BaseModel):
    token: str
    

class LoginUser(BaseModel):
    username: str
    password: str
