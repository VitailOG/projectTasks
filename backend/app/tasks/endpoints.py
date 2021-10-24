from typing import List
from fastapi import APIRouter, Depends

from core.db import database
from .models import task, column_task
from . import schemas
from .dependencies import get_column_service, get_task_service

router = APIRouter(
    prefix='/task'
)


@router.get('/test/{id}', response_model=List[schemas.Columns])
async def get_project_columns(
    id: int,
    _columns: column_task = Depends(get_column_service)
):
    colmns = await _columns.get_columns(id)
    return colmns


@router.post('/{id}')
async def create_column(
    id: int,
    item: schemas.CreateOrUpdateColumn,
    _columns: column_task = Depends(get_column_service)
):
    c_columns = await _columns.create_columns(item, id)
    return c_columns


@router.delete('/{id}')
async def delete_column(
    id: int,
    _columns: column_task = Depends(get_column_service)
):
    d_column = await _columns.delete_columns(id)
    return d_column


@router.patch('/{id}')
async def update_column(
    id: int,
    item: schemas.CreateOrUpdateColumn,
    _column: column_task = Depends(get_column_service)
):
    u_column = await _column.update_columns(item, id)
    return update_column


@router.post('/create/{id}')
async def create_task(
    id: int,
    item: schemas.CreateOrUpdateTask,
    _task: task = Depends(get_task_service)
):
    c_task = await _task.create_task(item, id)
    return c_task


@router.patch('/update/{id}')
async def update_task(
    id: int,
    item: schemas.CreateOrUpdateTask,
    _task: task = Depends(get_task_service)
):
    u_task = await _task.update_task(item, id)
    return u_task


@router.delete('/delete/{id}')
async def delete_task(
    id: int,
    _task: task = Depends(get_task_service)
):  
    d_task = await _task.delete_task(id)
    return d_task
