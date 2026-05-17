from enum import Enum


class Gender(str, Enum):
    MALE = "m"
    FEMALE = "f"


class IncomeType(str, Enum):
    WORKING = "working"
    COMMERCIAL_ASSOCIATION = "commercial_associate"
    STATE_SERVANT = "state_servant"
    PENSIONER = "pensioner"
    STUDENT = "student"


class EducationType(str, Enum):
    SECONDARY = "secondary"
    HIGHER = "higher_education"
    INCOMPLETE_HIGHER = "incomplete_higher"
    LOWER_SECONDARY = "lower_secondary"
    ACADEMIC_DEGREE = "academic_degree"


class FamStatus(str, Enum):
    MARRIED = "married"
    SINGLE = "single"
    CIVIL_MARRIAGE = "civil_marriage"
    SEPARATED = "separated"
    WIDOW = "widow"


class HousingType(str, Enum):
    HOUSE = "house"
    RENTED_APARTMENT = "rented_apartment"
    MUNICIPAL_APARTMENT = "municipal_apartment"
    WITH_PARENTS = "with_parents"
    OFFICE_APARTMENT = "office_apartment"
    COOP_APARTMENT = "co-op_apartment"


class JobTitle(str, Enum):
    SECURITY_STAFF = "security_staff"
    SALES_STAFF = "sales_staff"
    ACCOUNTANTS = "accountants"
    LABORERS = "laborers"
    MANAGERS = "managers"
    DRIVERS = "drivers"
    CORE_STAFF = "core_staff"
    HIGH_SKILL_TECH_STAFF = "high_skill_tech_staff"
    CLEANING_STAFF = "cleaning_staff"
    PRIVATE_SERVICE_STAFF = "private_service_staff"
    COOKING_STAFF = "cooking_staff"
    LOW_SKILL_LABORERS = "low-skill_laborers"
    MEDICINE_STAFF = "medicine_staff"
    SECRETARIES = "secretaries"
    WAITERS = "waiters"
    HR_STAFF = "hr_staff"
    REALTY_AGENTS = "realty_agents"
    IT_STAFF = "it_staff"
