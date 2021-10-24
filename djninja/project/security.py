from django.contrib.auth import get_user_model
from django.conf import settings

from ninja.security import HttpBearer

from jose import jwt
from datetime import datetime, timedelta

User = get_user_model()


def create_access_token(data: dict) -> str:
    encode_data: dict = data.copy()
    encode_data.update({"exp": datetime.utcnow() + timedelta(days=settings.EXPIRE_ACCESS_TOKEN)})
    return jwt.encode(encode_data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token: str) -> str:
    try:
        user_date = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except jwt.JWSError:
        user_date = None
    return user_date


def get_current_user(token):
    user_date = decode_access_token(token=token)
    print(user_date)
    return User.objects.filter(username=user_date.get('username')).first()


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        print(token)
        user = get_current_user(token=token)
        if user:
            return user
        return None