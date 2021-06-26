from typing import List, Optional
from pydantic import BaseModel


class Vacuna(BaseModel):
    sexo: str
    grupo_etario:str
    jurisdiccion_residencia: str
    jurisdiccion_residencia_id : str
    depto_residencia : str
    depto_residencia_id : str
    jurisdiccion_aplicacion : str
    jurisdiccion_aplicacion_id : int
    depto_aplicacion : str
    depto_aplicacion_id : int
    fecha_aplicacion : str
    vacuna : str
    condicion_aplicacion : str
    orden_dosis : int
    lote_vacuna : str
    class Config:
        orm_mode = True




