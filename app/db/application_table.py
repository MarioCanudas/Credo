from models import ApplicationBase
from sqlmodel import Field


class Applications(ApplicationBase, table=True):
    application_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id", index=True)
