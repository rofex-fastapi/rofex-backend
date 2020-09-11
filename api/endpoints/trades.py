from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import trade_crud
from models import trade_model
from schemas import  trade_schema
from api import deps

router = APIRouter()

@router.post("/trade/", response_model=trade_schema.TradeBase)
def get_trade(trade_id: int, db: Session = Depends(deps.get_db)):
    trade = trade_crud.get_trade(db=db, trade_id=trade_id)
    return trade

#Deberia devolver tambien el ID de trade
@router.post("/trades/", response_model=List[trade_schema.TradeBase])
def read_users(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    trades = trade_crud.get_trades(user_id=user_id, db=db, skip=skip, limit=limit)
    return trades

@router.post("/create-trade/", response_model=trade_schema.TradeBase)
def create_trade(trade: trade_schema.TradeBase, db: Session = Depends(deps.get_db)):
    return trade_crud.create_trade(db=db, trade=trade)