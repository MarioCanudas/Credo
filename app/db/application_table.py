from models import ApplicationBase
from sqlmodel import Field


class ApplicationTable(ApplicationBase, table=True):
    __tablename__ = "applications"

    application_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id", index=True)
