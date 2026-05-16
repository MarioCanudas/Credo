from contextlib import asynccontextmanager

from fastapi import FastAPI
from services import DBConnectionService


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_service = DBConnectionService()
    db_service.connect()
    yield
    db_service.disconnect()


app = FastAPI(lifespan=lifespan)
