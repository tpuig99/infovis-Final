from sqlalchemy.orm import Session
from . import models, schemas


def get_vacuna_by_sex(db: Session, sex: str):

    return db.query(models.Vacuna).filter(models.Vacuna.sexo == sex).all()


def get_vacuna_by_type(db: Session, type: str):

    return db.query(models.Vacuna).filter(models.Vacuna.vacuna == type).first()


def get_all_vacunas(db: Session, skip: int = 0, limit: int = 100):
    result = db.query(models.Vacuna).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return result


