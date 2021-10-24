from typing import List

from ninja import Router

from ..schemas import Columns, CreateOrUpdateTask, CreateOrUpdateColumn
from ..models import Column, Task
from ..security import User, AuthBearer

api = Router()


@api.get('/test/{id}', response=List[Columns], tags=['columns'], auth=AuthBearer())
def get_colmns_of_project(
    request, 
    id: int, 
):
    if request.auth:
        columns = Column.objects.filter(project=id).prefetch_related('tasks')
        return columns


@api.post('/{id}', tags=['columns'], auth=AuthBearer())
def create_columns(
    request, 
    id: int,
    item: CreateOrUpdateColumn 
):
    if request.auth:
        column = Column.objects.create(
            project_id=id,
            **item.dict()
        )
        return {"Created": True, "id": column.id}



@api.patch('/{id}', tags=['columns'], auth=AuthBearer())
def update_columns(
    request, 
    id: int,
    item: CreateOrUpdateColumn 
):
    if request.auth:
        Column.objects.filter(id=id)\
            .update(**item.dict())
        return {"update": True}


@api.delete('/{id}', tags=['columns'], auth=AuthBearer())
def delete_columns(
    request, 
    id: int
):
    if request.auth:
        Column.objects.filter(id=id)\
            .delete()
        return {"Delete": True}


@api.post('/create/{id}', tags=['task'], auth=AuthBearer())
def create_task(
    request,
    id: int,
    item: CreateOrUpdateTask
):
    if request.auth:
        task = Task.objects.create(
            column_id=id,
            **item.dict()
        )
        return {"Created": True, "id": task.id}


@api.patch('/update/{id}', tags=['task'], auth=AuthBearer())
def update_task(
    request,
    id: int,
    item: CreateOrUpdateTask 
):
    if request.auth:
        Task.objects.filter(id=id)\
            .update(
                **item.dict()
            )
        return {"Update": True}


@api.delete('/delete/{id}', tags=['task'], auth=AuthBearer())
def delete_task(
    request,
    id: int,
):
    if request.auth:
        Task.objects.filter(id=id).delete()
        return {"Delete": True}
