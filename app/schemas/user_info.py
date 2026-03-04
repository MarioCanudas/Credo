from enum import Enum
from typing import Literal

import pandas as pd
from enums import EducationType, FamStatus, Gender, HousingType, IncomeType, JobTitle
from pydantic import BaseModel, field_validator


class UserInfo(BaseModel):
    gender: Gender
    car: Literal[0, 1]
    realty: Literal[0, 1]
    cnt_children: int
    income: int
    income_type: IncomeType
    education_type: EducationType
    fam_status: FamStatus
    housing_type: HousingType
    mobile_phone: Literal[0, 1]
    work_phone: Literal[0, 1]
    phone: Literal[0, 1]
    email: Literal[0, 1]
    job_title: JobTitle
    cnt_fam_members: int
    age: int
    work_experience: int
    bad_debt: int
    good_debt: int

    @field_validator("income")
    def validate_income(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Income must be non-negative")
        return value

    @field_validator("cnt_children")
    def validate_cnt_children(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Count of children must be non-negative")
        return value

    @field_validator("cnt_fam_members")
    def validate_cnt_fam_members(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Count of family members must be non-negative")
        return value

    @field_validator("age")
    def validate_age(cls, value: int) -> int:
        if value < 18:
            raise ValueError("Age must be at least 18")
        return value

    @field_validator("work_experience")
    def validate_work_experience(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Work experience must be non-negative")
        return value

    def to_dataframe(self) -> pd.DataFrame:
        dump = self.model_dump()

        for k, v in dump.items():
            if isinstance(v, Enum):
                dump[k] = [v.value]
            else:
                dump[k] = [v]

        return pd.DataFrame(dump)
