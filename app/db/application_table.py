from models import ApplicationBase
from sqlmodel import Field


class ApplicationTable(ApplicationBase, table=True):
    application_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="usertable.user_id", index=True)
