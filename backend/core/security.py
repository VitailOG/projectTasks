from jose import jwt
from typing import Optional

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException, status, Depends

from datetime import datetime, timedelta
from passlib.context import CryptContext

from .db import EXPIRE_ACCESS_TOKEN, SECRET_KEY, ALGORITHM
from .db import database
from app.auth.models import user


ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return ctx.hash(password)


def verify_password(password: str, hash: str) -> bool:
    return ctx.verify(password, hash)


def create_access_token(data: dict) -> str:
    encode_data: dict = data.copy()
    encode_data.update({"exp": datetime.utcnow() + timedelta(days=EXPIRE_ACCESS_TOKEN)})
    return jwt.encode(encode_data, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> str:
    try:
        user_date = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except jwt.JWSError:
        user_date = None
    return user_date


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        exp = HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            token = decode_access_token(credentials.credentials)
            print(token)
            if token is None:
                raise exp
            return credentials.credentials
        else:
            raise exp


async def get_current_user(jwt: str = Depends(JWTBearer())):
    payload = decode_access_token(jwt)
    c_user = await database.fetch_one(user.select().where(user.c.username == payload.get('username')))   
    return c_user
