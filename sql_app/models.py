from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


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


