from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.endpoints import router as auth_router
from app.project.endpoints import router as project_router
from app.tasks.endpoints import router as tasks_router
from core.db import database


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.include_router(auth_router, tags=['auth'])
app.include_router(project_router, tags=['project'])
app.include_router(tasks_router, tags=['tasks'])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

from core.db import database
from app.project.models import project
from app.tasks.models import task, column_task

@app.get("/del", tags=['delete'])
async def d():
    q = project.delete()
    await database.execute(q)
    return 0

@app.post("/all", tags=['delete'])
async def a():
    q = project.select()
    p = await database.fetch_all(q)
    return p


@app.get("/del1", tags=['delete'])
async def d1():
    q = column_task.delete()
    await database.execute(q)
    return 0


@app.post("/all1", tags=['delete'])
async def a1():
    q = column_task.select()
    p = await database.fetch_all(q)
    return p


@app.get("/del2", tags=['delete'])
async def d2():
    q = task.delete()
    await database.execute(q)
    return 0


@app.post("/all2", tags=['delete'])
async def a1():
    q = task.select()
    p = await database.fetch_all(q)
    return p
