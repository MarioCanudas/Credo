from models import UserBase
from sqlmodel import Field


class UserTable(UserBase, table=True):
    __tablename__ = "users"

    user_id: int | None = Field(default=None, primary_key=True)
