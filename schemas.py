from typing import List, Optional

from pydantic import BaseModel

#Esto seria base
class UserBase(BaseModel):
    email: str

#Esto para crear
class UserCreate(UserBase):
    password: str

#Esto para leer (devolver desde la API), por eso no tiene pass
class User(UserBase):
    id: int
    name: str
    lastname: str

    #config de Pydantic
    class Config:
        orm_mode = True