from database.database import SessionLocal, engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from models import user_model

#start database
user_model.Base.metadata.create_all(bind=engine)

def get_db(): #averiguar -> Generator
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

