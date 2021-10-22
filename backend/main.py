from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.endpoints import router as auth_router
from app.project.endpoints import router as project_router
from app.tasks.endpoints import router as tasks_router
from core.db import database


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router, tags=['auth'])
app.include_router(project_router, tags=['project'])
app.include_router(tasks_router, tags=['tasks'])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
