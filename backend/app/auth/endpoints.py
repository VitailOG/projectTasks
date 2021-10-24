from fastapi import APIRouter, HTTPException, status, Depends

from .models import user
from . import schemas

from core.security import get_current_user
from .dependencies import get_auth_service


from core.db import database
router = APIRouter(
    prefix='/auth'
)


@router.get('/')
async def all(
    current_user: user = Depends(get_current_user)
):
    return await database.fetch_all(user.select())


@router.post('/', response_model=schemas.Token)
async def login(
    login: schemas.LoginUser,
    user: user = Depends(get_auth_service)
) -> dict:
    user_token = await user.login(login)
    return user_token


@router.post('/create')
async def register(
    item: schemas.CreateUser,
    c_user: user = Depends(get_auth_service)
):
    _user = await c_user.create_user(item)
    if _user:
        return _user

