from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id : Optional[str] = None 
    name : str
    description : str
    price : float
    id_cliente : int