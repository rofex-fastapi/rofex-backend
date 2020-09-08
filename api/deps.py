from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from database.database import SessionLocal, engine
from models import user_model
from schemas import user_schema, token_schema
from crud import user_crud

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#start database
user_model.Base.metadata.create_all(bind=engine)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 

# def get_current_user(
#     db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
# ) -> user_model.User:
#     try:
#         payload = jwt.decode(
#             token, SECRET_KEY, algorithms=["HS256"]
#         )
#         token_data = token_schema.TokenPayload(**payload)
#     except (jwt.JWTError, ValidationError):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#         )
#     user = user_crud.User.get_user_for_validation(db, user_email=)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user