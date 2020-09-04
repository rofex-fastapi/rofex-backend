from sqlalchemy.orm import Session

from models import user_model
from schemas import user_schema

#READ
def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()

#CREATE
def create_user(db: Session, user: user_schema.UserCreate):
    hashed_pass = user.hashed_password #aca hacer el hash
    db_user = user_model.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



