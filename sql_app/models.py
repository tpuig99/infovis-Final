from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from enum import Enum

class Vacuna(Base):

    __tablename__ = "vacunas"

    id = Column(Integer, primary_key=True)
    sexo = Column(String)
    grupo_etario = Column(String)
    jurisdiccion_residencia = Column(String)
    jurisdiccion_residencia_id = Column(Integer)
    depto_residencia = Column(String)
    depto_residencia_id = Column(Integer)
    jurisdiccion_aplicacion = Column(String)
    jurisdiccion_aplicacion_id = Column(Integer)
    depto_aplicacion = Column(String)
    depto_aplicacion_id = Column(Integer)
    fecha_aplicacion = Column(String)
    vacuna = Column(String)
    condicion_aplicacion = Column(String)
    orden_dosis = Column(Integer)
    lote_vacuna = Column(String)


class ModelCondiciones(str, Enum):
    salud = "Salud"
    estrategico = "Estratégico"
    otros = "Otros"
    riesgo = "18 a 59 años CON Factores de Riesgo"
    mencuarentaS = "18 a 39 años SIN Factores de Riesgo"
    cuarentaS = "40 a 49 años SIN Factores de Riesgo"
    cincuentaS = "50 a 59 años SIN Factores de Riesgo"
    sesenta = "60 o más años"

class ModelSex(str, Enum):
    femenino = "F"
    masculino = "M"

class ModelVacunas(str, Enum):
    COVISHIELD = "COVISHIELD"
    Sinopharm = "Sinopharm"
    Sputnik = "Sputnik"
    AstraZeneca = "AstraZeneca"

class ModelAge(str, Enum):
    desconocido = "S.I."
    veintes = "18-29"
    treintas = "30-39"
    cuarentas = "40-49"
    cincuentas = "50-59"
    sesentas = "60-69"    
    setentas = "70-79"
    ochentas = "80-89"
    noventas = "90-99"
    gcien = ">=100"



