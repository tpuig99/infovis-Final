from typing import Optional
from sqlalchemy.orm import Session
from . import models, schemas

#########################   Individual metrics #########################
## Sex ##
def get_vacuna_by_sex(db: Session, sex: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.sexo == sex).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.sexo == sex).all()


def get_vacuna_by_sex_count(db: Session, sex: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.sexo == sex).count()


## Condition ##
def get_vacuna_by_condition(db: Session, condition: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.condicion_aplicacion == condition).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.condicion_aplicacion == condition).all()


def get_vacuna_by_condition_count(db: Session, condition: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.condicion_aplicacion == condition).count()


## Age ##
def get_vacuna_by_age(db: Session, age: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.grupo_etario == age).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.grupo_etario == age).all()


def get_vacuna_by_age_count(db: Session, age: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.grupo_etario == age).count()


## Provincia de residencia ##
def get_vacuna_by_residence_provincia(db: Session, provincia: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_residencia == provincia).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_residencia == provincia).all()


def get_vacuna_by_residence_provincia_count(db: Session, provincia: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.jurisdiccion_residencia == provincia).count()


## Provincia de aplicacion ##
def get_vacuna_by_aplication_provincia(db: Session, provincia: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia).all()


def get_vacuna_by_aplication_provincia_count(db: Session, provincia: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.jurisdiccion_aplicacion == provincia).count()


## Vaccine type ##
def get_vacuna_by_marca(db: Session, marca: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.vacuna == marca).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.vacuna == marca).all()


def get_vacuna_by_marca_count(db: Session, marca: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.vacuna == marca).count()


## Dosis ##
def get_vacuna_by_dosis(db: Session, dosis: int, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.orden_dosis == dosis).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.orden_dosis == dosis).all()


def get_vacuna_by_dosis_count(db: Session, dosis: int):
    return db.query(models.Vacuna.id).filter(models.Vacuna.orden_dosis == dosis).count()


## Misc ##
def get_vacuna_by_type(db: Session, type: str):
    return db.query(models.Vacuna).filter(models.Vacuna.vacuna == type).first()


def get_all_vacunas(db: Session, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).all()


def get_all_vacunas_count(db: Session):
    result = db.query(models.Vacuna.id).count()
    return result


#########################   Double metrics #########################
### Age + other ###
def get_vacuna_by_age_condition(db: Session, age: str, condition: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.grupo_etario == age, models.Vacuna.condicion_aplicacion == condition).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.grupo_etario == age, models.Vacuna.condicion_aplicacion == condition).all()


def get_vacuna_by_age_condition_count(db: Session, age: str, condition: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.grupo_etario == age, models.Vacuna.condicion_aplicacion == condition).count()


def get_vacuna_by_age_provincia(db: Session, age: str, provincia: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.grupo_etario == age, models.Vacuna.jurisdiccion_aplicacion == provincia).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.grupo_etario == age, models.Vacuna.jurisdiccion_aplicacion == provincia).all()


def get_vacuna_by_age_provincia_count(db: Session, age: str, provincia: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.grupo_etario == age, models.Vacuna.jurisdiccion_aplicacion == provincia).count()


def get_vacuna_by_age_vacuna(db: Session, age: str, vacuna: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.grupo_etario == age, models.Vacuna.vacuna == vacuna).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.grupo_etario == age, models.Vacuna.vacuna == vacuna).all()


def get_vacuna_by_age_vacuna_count(db: Session, age: str, vacuna: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.grupo_etario == age, models.Vacuna.vacuna == vacuna).count()


def get_vacuna_by_age_dosis(db: Session, age: str, dosis: int, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.grupo_etario == age, models.Vacuna.orden_dosis == dosis).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.grupo_etario == age, models.Vacuna.orden_dosis == dosis).all()


def get_vacuna_by_age_dosis_count(db: Session, age: str, dosis: int):
    return db.query(models.Vacuna.id).filter(models.Vacuna.grupo_etario == age, models.Vacuna.orden_dosis == dosis).count()


### Vaccine type + other ###
def get_vacuna_by_vacuna_provincia(db: Session, provincia: str, vacuna: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.vacuna == vacuna).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.vacuna == vacuna).all()


def get_vacuna_by_vacuna_provincia_count(db: Session, provincia: str, vacuna: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.vacuna == vacuna).count()


def get_vacuna_by_vacuna_dosis(db: Session, dosis: int, vacuna: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna).all()


def get_vacuna_by_vacuna_dosis_count(db: Session, dosis: int, vacuna: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna).count()


## Provincia + other ##
def get_vacuna_by_provincia_fecha(db: Session, provincia: str, fecha: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.fecha_aplicacion == fecha).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.fecha_aplicacion == fecha).all()


def get_vacuna_by_provincia_fecha_count(db: Session, provincia: str, fecha: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.fecha_aplicacion == fecha).count()


def get_vacuna_by_provincia_dosis(db: Session, provincia: str, dosis: int, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.orden_dosis == dosis).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.orden_dosis == dosis).all()


def get_vacuna_by_provincia_dosis_count(db: Session, provincia: str, dosis: int):
    return db.query(models.Vacuna.id).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.orden_dosis == dosis).count()


### Condition + other ###
def get_vacuna_by_condicion_provincia(db: Session, condicion: str, provincia: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.condicion_aplicacion == condicion, models.Vacuna.jurisdiccion_residencia == provincia).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.condicion_aplicacion == condicion, models.Vacuna.jurisdiccion_residencia == provincia).all()


def get_vacuna_by_condicion_provincia_count(db: Session, condicion: str, provincia: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.condicion_aplicacion == condicion, models.Vacuna.jurisdiccion_residencia == provincia).count()


def get_vacuna_by_condicion_dosis(db: Session, condicion: str, dosis: int, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.condicion_aplicacion == condicion, models.Vacuna.orden_dosis == dosis).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.condicion_aplicacion == condicion, models.Vacuna.orden_dosis == dosis).all()


def get_vacuna_by_condicion_dosis_count(db: Session, condicion: str, dosis: int):
    return db.query(models.Vacuna.id).filter(models.Vacuna.condicion_aplicacion == condicion, models.Vacuna.orden_dosis == dosis).count()


def get_vacuna_by_condicion_vacuna(db: Session, condicion: str, vacuna: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.condicion_aplicacion == condicion, models.Vacuna.vacuna == vacuna).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.condicion_aplicacion == condicion, models.Vacuna.vacuna == vacuna).all()


def get_vacuna_by_condicion_vacuna_count(db: Session, condicion: str, vacuna: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.condicion_aplicacion == condicion, models.Vacuna.vacuna == vacuna).count()


#########################   Triple metrics #########################
## Vacuna - Dosis - Condicion ##
def get_vacuna_by_vacuna_dosis_condition(db: Session, dosis: int, vacuna: str, condition: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna, models.Vacuna.condicion_aplicacion == condition).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna, models.Vacuna.condicion_aplicacion == condition).all()


def get_vacuna_by_vacuna_dosis_condition_count(db: Session, dosis: int, vacuna: str, condition: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna, models.Vacuna.condicion_aplicacion == condition).count()


## Vacuna - Dosis - Provincia ##
def get_vacuna_by_vacuna_dosis_provincia(db: Session, dosis: int, vacuna: str, provincia: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna, models.Vacuna.jurisdiccion_aplicacion == provincia).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna, models.Vacuna.jurisdiccion_aplicacion == provincia).all()


def get_vacuna_by_vacuna_dosis_provincia_count(db: Session, dosis: int, vacuna: str, provincia: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna, models.Vacuna.jurisdiccion_aplicacion == provincia).count()


## Vacuna - Dosis - Edad ##
def get_vacuna_by_vacuna_dosis_age(db: Session, dosis: int, vacuna: str, age: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna, models.Vacuna.grupo_etario == age).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna, models.Vacuna.grupo_etario == age).all()


def get_vacuna_by_vacuna_dosis_age_count(db: Session, dosis: int, vacuna: str, age: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.orden_dosis == dosis, models.Vacuna.vacuna == vacuna, models.Vacuna.grupo_etario == age).count()


## Vacuna - Provincia - Fecha ##
def get_vacuna_by_vacuna_provincia_fecha(db: Session, provincia: str, vacuna: str, fecha: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.vacuna == vacuna, models.Vacuna.fecha_aplicacion == fecha).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.vacuna == vacuna, models.Vacuna.fecha_aplicacion == fecha).all()


def get_vacuna_by_vacuna_provincia_fecha_count(db: Session,  provincia: str, vacuna: str, fecha: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.vacuna == vacuna, models.Vacuna.fecha_aplicacion == fecha).count()


## Vacuna - Provincia - Fecha ##
def get_vacuna_by_vacuna_provincia_dosis_fecha(db: Session, provincia: str, vacuna: str, dosis: int, fecha: str, skip: int = 0, limit: Optional[int] = None):
    if limit:
        return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.vacuna == vacuna, models.Vacuna.orden_dosis == dosis, models.Vacuna.fecha_aplicacion == fecha).order_by(models.Vacuna.id).offset(skip).limit(limit).all()
    return db.query(models.Vacuna).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.vacuna == vacuna, models.Vacuna.orden_dosis == dosis, models.Vacuna.fecha_aplicacion == fecha).all()


def get_vacuna_by_vacuna_provincia_dosis_fecha_count(db: Session,  provincia: str, vacuna: str, dosis: int, fecha: str):
    return db.query(models.Vacuna.id).filter(models.Vacuna.jurisdiccion_aplicacion == provincia, models.Vacuna.vacuna == vacuna, models.Vacuna.orden_dosis == dosis, models.Vacuna.fecha_aplicacion == fecha).count()
