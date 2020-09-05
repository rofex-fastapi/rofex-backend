from fastapi import FastAPI
from api.endpoints import login, users

app = FastAPI(
  title="FastAPI - Name not defined",
  description="FastAPI - Login for rofex example",
  version="0.0.1"
)

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"API": "made by eche",
            "Help": "go to /docs"
    }


