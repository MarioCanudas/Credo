import pathlib
import sys

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

# Add 'app' directory to sys.path
root_path = pathlib.Path(__file__).parent.parent
sys.path.append(str(root_path / "app"))

from app.api import get_session
from app.enums import (
    EducationType,
    FamStatus,
    Gender,
    HousingType,
    IncomeType,
    JobTitle,
)
from app.main import app

# Setup in-memory database for testing
DATABASE_URL = "sqlite://"


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def load_test_data(n_rows=10):
    csv_path = root_path / "ml_engine" / "training" / "data" / "test.csv"
    df = pd.read_csv(csv_path).head(n_rows)

    formatted_data = []
    for _, row in df.iterrows():
        user_payload = {
            "gender": Gender(row["gender"]).value,
            "car": bool(row["car"]),
            "realty": bool(row["realty"]),
            "cnt_children": int(row["cnt_children"]),
            "income": int(row["income"]),
            "income_type": IncomeType(row["income_type"]).value,
            "education_type": EducationType(row["education_type"]).value,
            "fam_status": FamStatus(row["fam_status"]).value,
            "housing_type": HousingType(row["housing_type"]).value,
            "mobile_phone": bool(row["mobile_phone"]),
            "work_phone": bool(row["work_phone"]),
            "phone": bool(row["phone"]),
            "email": bool(row["email"]),
            "job_title": JobTitle(row["job_title"]).value,
            "cnt_fam_members": int(row["cnt_fam_members"]),
            "age": int(row["age"]),
            "work_experience": int(row["work_experience"]),
            "bad_debt": int(row["bad_debt"]),
            "good_debt": int(row["good_debt"]),
        }
        formatted_data.append((int(row["id"]), user_payload))
    return formatted_data


@pytest.mark.parametrize("original_id, user_payload", load_test_data())
def test_create_user_and_application(client: TestClient, original_id, user_payload):
    # 1. Create User
    # We use a custom user_id if needed, but the API creates its own if not provided?
    # Actually, Users model in DB has user_id: int | None = Field(default=None, primary_key=True)
    # But UserBase doesn't have it. So the API will let DB generate it OR we can provide it if we add it to the payload.
    # Looking at create_user: db_user = Users.model_validate(user).
    # If we want to keep the original_id for reference, we might need to add it to UserBase or handle it.
    # For testing, we'll just let the API create a user and use that ID.

    response = client.post("/users/", json=user_payload)
    assert response.status_code == 200
    user_data = response.json()
    user_id = user_data["user_id"]
    assert user_id is not None

    # 2. Create Application
    app_payload = {"user_id": user_id}
    app_response = client.post("/applications/", json=app_payload)
    assert app_response.status_code == 200
    app_data = app_response.json()
    assert app_data["user_id"] == user_id
    assert "status" in app_data
    assert app_data["status"] in ["approved", "rejected"]

    # 3. Get Application Status
    get_response = client.get(f"/applications/{user_id}")
    assert get_response.status_code == 200
    assert get_response.json()["status"] == app_data["status"]
