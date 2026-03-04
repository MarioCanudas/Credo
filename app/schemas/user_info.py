from typing import Literal

from enums import EducationType, FamStatus, Gender, HousingType, IncomeType, JobTitle
from services import MLService
from pydantic import BaseModel, field_validator
import numpy as np


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

    @property
    def ml_service(self) -> MLService:
        return MLService()

    @property
    def categorical_info(self) -> list[str]:
        return [
            "gender",
            "income_type",
            "education_type",
            "fam_status",
            "housing_type",
            "job_title",
        ]

    @property
    def binary_info(self) -> list[str]:
        return [
            "car",
            "realty",
            "mobile_phone",
            "work_phone",
            "phone",
            "email",
        ]

    @property
    def numerical_info(self) -> list[str]:
        return [
            "cnt_children",
            "income",
            "cnt_fam_members",
            "age",
            "work_experience",
            "bad_debt",
            "good_debt",
        ]
