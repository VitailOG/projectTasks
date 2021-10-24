from ninja import Router


from ..schemas import AuthLogin
from ..security import AuthBearer, User, create_access_token

api = Router()


@api.post('/')
def login(request, item: AuthLogin):
    user = User.objects.filter(username=item.username).first()
    if user and user.check_password(item.password):
        token = create_access_token({"username": item.username})
        return {"token": token}
    return {"error": "user does not exist"}

