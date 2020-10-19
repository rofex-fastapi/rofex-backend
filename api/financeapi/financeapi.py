import pyRofex
from datetime import date
from typing import List, Union, Dict

user = "dbdamix3901" #os.environ["user"]
password = "melulI3)"
account = "REM3901"
        
pyRofex.initialize(user=user, password=password, account=account, environment=pyRofex.Environment.REMARKET)

def get_trade_history(trade_symbol: str)-> List[Dict[str, Union[float, str]]]: 
    return pyRofex.get_trade_history(trade_symbol, "2020-01-01", date.today())["trades"]