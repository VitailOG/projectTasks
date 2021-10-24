from typing import List

from fastapi import APIRouter, Depends

from ..auth.models import user
from core.security import get_current_user
from . import schemas
from .models import project
from .dependencies import get_project_service


router = APIRouter(
    prefix='/project'
)


@router.get('/', response_model=List[schemas.ListUserProject])
async def get_projects_user(
    current_user: user = Depends(get_current_user),
    project: project = Depends(get_project_service)
):
    user_projects = await project.list_user_project(current_user.id)
    return user_projects


@router.post('/')
async def create_project(
    item: schemas.CreateProject,
    current_user: user = Depends(get_current_user),
    _project: project = Depends(get_project_service)
):
    cp = await _project.create_project(item, current_user.id)
    return cp


@router.delete('/{id}')
async def delete_project(
    id: int,
    current_user: user = Depends(get_current_user),
    _project: project = Depends(get_project_service)
):  
    del_project = await _project.delete_project(id)
    return del_project


@router.patch('/{id}')
async def update_project(
    id: int,
    item: schemas.CreateProject,
    current_user: user = Depends(get_current_user),
    _project: project = Depends(get_project_service)
):
    modify_project = await _project.update_project(item, id)
    return modify_project
