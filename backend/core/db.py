from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi"

EXPIRE_ACCESS_TOKEN = 2
SECRET_KEY = "nHTDmqnpNldsSLm1iADgLyZgJO34YDS7"
ALGORITHM = "HS256"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

database = Database(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()


class BaseDB:
    def __init__(self, database: Database):
        self.database = database
        