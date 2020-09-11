from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

class TradeBase(BaseModel):
    symbol: str
    size: float
    price: float
    datetime: datetime
    iduser: int 
    
    class Config:
        orm_mode = True

class Trade(TradeBase):
    id: int
    class Config:
        orm_mode = True

