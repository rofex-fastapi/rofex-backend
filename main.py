import uvicorn

from fastapi import FastAPI
from api.router import api_router

app = FastAPI(
  title="FastAPI - Name not defined",
  description="FastAPI - Login for rofex example",
  version="0.0.1"
)

app.include_router(api_router)

#Debug
if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)