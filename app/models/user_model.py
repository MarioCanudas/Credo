from enums import EducationType, FamStatus, Gender, HousingType, IncomeType, JobTitle
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    gender: Gender
    car: bool
    realty: bool
    cnt_children: int = Field(ge=0)
    income: int = Field(gt=0)
    income_type: IncomeType
    education_type: EducationType
    fam_status: FamStatus
    housing_type: HousingType
    mobile_phone: bool
    work_phone: bool
    phone: bool
    email: bool
    job_title: JobTitle
    cnt_fam_members: int = Field(ge=0)
    age: int = Field(ge=18)
    work_experience: int = Field(ge=0)
    bad_debt: int = Field(ge=0)
    good_debt: int = Field(ge=0)
