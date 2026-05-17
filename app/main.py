from contextlib import asynccontextmanager

from api.routers import applications_router, users_router
from fastapi import FastAPI
from services import DBConnectionService


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_service = DBConnectionService()
    db_service.connect()
    yield
    db_service.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(users_router)
app.include_router(applications_router)
