from typing import Optional
from pydantic import BaseModel

class Alumno(BaseModel):
    id : Optional[str] = None   
    name : str
    surname : str
    birth_date : str
    curso : str
    repetidor : bool
    id_colegio : str