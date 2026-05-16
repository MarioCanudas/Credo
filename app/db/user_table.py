from models import UserBase
from sqlmodel import Field


class Users(UserBase, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
