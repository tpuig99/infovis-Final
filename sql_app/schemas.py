from typing import List, Optional
from pydantic import BaseModel


class Vacuna(BaseModel):
    sexo: str
    grupo_etario:str
    jurisdiccion_residencia: str
    jurisdiccion_aplicacion : str
    fecha_aplicacion : str
    vacuna : str
    condicion_aplicacion : str
    orden_dosis : int
    class Config:
        orm_mode = True




