from typing import List
from django.contrib.auth import get_user_model

from ninja import Router


from ..models import Project
from ..schemas import (
    CreateOrUpdateProject,
    Projects, 
)

from ..security import User, AuthBearer


api = Router()


@api.post('/', tags=['project'], auth=AuthBearer())
def create_project(request, item: CreateOrUpdateProject):
    if request.auth is not None:
        project = Project.objects.create(
            **item.dict(), 
            user=request.auth
        )
        return {"success": True, 'id': project.id}
    return {"error": 401}


@api.get('/', response=List[Projects], tags=['project'], auth=AuthBearer())
def get_user_projects(request):
    if request.auth:
        projects = Project.objects.filter(user=request.auth)
        return projects


@api.patch('/{id}', tags=['project'], auth=AuthBearer())
def change_title_project(
    request, 
    id: int, 
    item: CreateOrUpdateProject
):
    if request.auth:
        Project.objects\
            .filter(id=id)\
            .update(**item.dict())
        return {'update': True}


@api.delete('/{id}', tags=['project'], auth=AuthBearer())
def delete_project(
    request, 
    id: int, 
):
    if request.auth:
        Project.objects\
            .filter(id=id)\
            .delete()
        return {'delete': True}
