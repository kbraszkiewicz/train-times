from dataclasses import dataclass
from typing import Optional

@dataclass
class Stop:
    name:str
    arival_time:str

@dataclass
class Train:
    departue_station: str
    final_station:str
    due_time:str
    status:str
    platform:str
    stops:list[Stop]
    on_time: Optional[bool] = False

@dataclass
class Board:
    station:str
    trains:list[Train]