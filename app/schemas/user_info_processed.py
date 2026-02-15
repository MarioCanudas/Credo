from typing import Literal

from pydantic import BaseModel


class UserInfoProcessed(BaseModel):
    phone: Literal[0, 1]
