from database.database import SessionLocal, engine

from models import user_model

user_model.Base.metadata.create_all(bind=engine)

def get_db(): #averiguar -> Generator
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

