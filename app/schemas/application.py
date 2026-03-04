from pydantic import BaseModel

from .user_info import UserInfo


class Application(BaseModel):
    token: str
    user_id: int
    user_info: UserInfo
