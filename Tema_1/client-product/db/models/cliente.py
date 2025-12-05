from typing import Optional
from pydantic import BaseModel

class Cliente(BaseModel):
    id : Optional[str] = None   
    dni: str
    name : str
    surname : str
    phone : int
    email : str