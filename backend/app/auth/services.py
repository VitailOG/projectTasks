from fastapi import Depends, HTTPException, status

from core.db import BaseDB
from .models import user
from core.security import hash_password, create_access_token, verify_password


class AuthService(BaseDB):

    async def login(self, login):
        _user = await self.database.fetch_one(user.select().where(user.c.username == login.username))
        if _user is None or not verify_password(login.hashed_password, _user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        _user
        token = create_access_token({"username": _user.username})
        return {"token": token}

    async def create_user(self, item: user) -> user:
        _user = user.insert().values(
            email=item.email,
            username=item.username,
            is_active=item.is_active,
            hashed_password=hash_password(item.hashed_password)
        )
        print(hash_password(item.hashed_password))
        await self.database.execute(_user)
        return True

