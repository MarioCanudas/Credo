from pydantic import BaseModel
from utils import process_user_info

from .user_info import UserInfo
from .user_info_processed import UserInfoProcessed


class Application(BaseModel):
    token: str
    user_id: int
    user_info: UserInfo

    def process_info(self) -> UserInfoProcessed:
        return process_user_info(self.user_info)
