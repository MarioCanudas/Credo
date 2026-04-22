from datetime import datetime

from enums import ApplicationStatus
from sqlmodel import SQLModel


class ApplicationBase(SQLModel):
    user_id: int
    application_date: datetime
    status: ApplicationStatus
