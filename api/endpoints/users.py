from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import user_crud
from models import user_model
from schemas import  user_schema
from api import deps


router = APIRouter()


@router.get("/users/", response_model=List[user_schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    """
    Retrieve all the users.
    """
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users

@router.post("/users/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(deps.get_db)):
    """
    Create new user.
    """
    db_user = user_crud.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)