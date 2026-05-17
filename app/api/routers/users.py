from api import get_session
from db import Users
from fastapi import APIRouter, Depends, HTTPException
from models import UserBase
from sqlmodel import Session

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/", response_model=Users)
def create_user(user: UserBase, session: Session = Depends(get_session)):
    db_user = Users.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@users_router.get("/{user_id}", response_model=Users)
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users_router.put("/{user_id}", response_model=Users)
def update_user(
    user_id: int, user_data: UserBase, session: Session = Depends(get_session)
):
    db_user = session.get(Users, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update user data
    new_data = user_data.model_dump(exclude_unset=True)
    for key, value in new_data.items():
        setattr(db_user, key, value)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@users_router.delete("/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    session.delete(user)
    session.commit()
    return {
        "message": f"User with ID {user_id} and all associated data have been deleted successfully"
    }
