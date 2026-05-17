from datetime import datetime

from api import get_session
from db import Applications, Users
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from services import MLService
from sqlmodel import Session, select

applications_router = APIRouter(prefix="/applications", tags=["applications"])


class ApplicationCreate(BaseModel):
    user_id: int


@applications_router.post("/", response_model=Applications)
def create_application(
    payload: ApplicationCreate, session: Session = Depends(get_session)
):
    # Check if user exists
    user = session.get(Users, payload.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if application already exists
    existing_app = session.exec(
        select(Applications).where(Applications.user_id == payload.user_id)
    ).first()
    if existing_app:
        raise HTTPException(
            status_code=400, detail="Application already exists for this user"
        )

    # Predict status
    ml_service = MLService()
    status = ml_service.predict_application(user)

    # Create application
    db_application = Applications(
        user_id=payload.user_id, application_date=datetime.now(), status=status
    )
    session.add(db_application)
    session.commit()
    session.refresh(db_application)
    return db_application


@applications_router.get("/{user_id}", response_model=Applications)
def get_application_status(user_id: int, session: Session = Depends(get_session)):
    application = session.exec(
        select(Applications).where(Applications.user_id == user_id)
    ).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application
