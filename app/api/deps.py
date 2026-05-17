from collections.abc import Generator

from services import DBConnectionService
from sqlmodel import Session


def get_session() -> Generator[Session]:
    db_service = DBConnectionService()
    if db_service.engine is None:
        db_service.connect()
    with Session(db_service.engine) as session:
        yield session
