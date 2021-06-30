from typing import List, Optional
from fastapi import Depends, FastAPI, Query, Path
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

############ Endpoints Description #############
tags_metadata = [
    {"name": "General Vacunas", "description": "Obtiene las vacunas sin ningún filtro."},
    {"name": "Vacunas solo por sexo",
        "description": "Obtiene las vacunas filtradas por sexo."},
    {"name": "Vacunas solo por edad",
        "description": "Obtiene las vacunas filtradas por grupo etario."},
    {"name": "Vacunas solo por condicion",
        "description": "Obtiene las vacunas filtradas por la condición de la aplicación."},
    {"name": "Vacunas solo por provincia de residencia",
        "description": "Obtiene las vacunas filtradas por la jurisdicción/provincia de residencia."},
    {"name": "Vacunas solo por marca de vacuna suministrada",
        "description": "Obtiene las vacunas filtradas por la marca de la vacuna suministrada."},
    {"name": "Vacunas solo por número de dosis",
        "description": "Obtiene las vacunas filtradas por si es primera o segunda dosis."},
    {"name": "Vacunas solo por provincia donde se aplició la dosis",
        "description": "Obtiene las vacunas filtradas por la jursidicción/provincia en la que se aplicó la dosis."},
    {"name": "Vacunas por condición y otro factor",
        "description": "Obtiene las vacunas filtradas por condición y: provincia, dosis, vacuna."},
    {"name": "Vacunas por provincia y otro factor",
        "description": "Obtiene las vacunas filtradas por provincia y: fecha."},
    {"name": "Vacunas por edad y otro factor",
        "description": "Obtiene las vacunas filtradas por grupo etario y: condición de aplicación, provincia, vacuna, dosis."},
    {"name": "Vacunas por vacuna y otro factor",
        "description": "Obtiene las vacunas filtradas por la vacuna y: dosis, provincia, condicion y dosis, provincia y dosis."},
]


models.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Final Infovis - Vacunas COVID19",
    description="Esta API permite obtener información acerca de la vacunación por el COVID19 en Argentina.",
    openapi_tags=tags_metadata)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


#########################   Individual metrics #########################
# All
@app.get("/vacunas/", response_model=List[schemas.Vacuna], tags=["General Vacunas"])
def read_vacunas(skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    return crud.get_all_vacunas(db, skip=skip, limit=limit)


@app.get("/vacunas/count", tags=["General Vacunas"])
def read_vacunas(db: Session = Depends(get_db)):
    return crud.get_all_vacunas_count(db)


# Sex
@app.get("/vacunas/sex/{sex}", response_model=List[schemas.Vacuna], tags=["Vacunas solo por sexo"])
def read_vacunas(sex: models.ModelSex, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_sex(db, sex, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/sex/{sex}/count", tags=["Vacunas solo por sexo"])
def read_vacunas(sex: models.ModelSex, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_sex_count(db, sex)
    return vacunas


# Condition
@app.get("/vacunas/condition/{condition}", response_model=List[schemas.Vacuna], tags=["Vacunas solo por condicion"])
def read_vacunas(condition: models.ModelCondiciones, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_condition(db, condition, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/condition/{condition}/count", tags=["Vacunas solo por condicion"])
def read_vacunas(condition: models.ModelCondiciones, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_condition_count(db, condition)
    return vacunas


# Age
@app.get("/vacunas/age/{age}", response_model=List[schemas.Vacuna], tags=["Vacunas solo por edad"])
def read_vacunas(age: models.ModelAge, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age(db, age, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/age/{age}/count", tags=["Vacunas solo por edad"])
def read_vacunas(age: models.ModelAge, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_sex_count(db, age)
    return vacunas


# Residence Province
@app.get("/vacunas/provincia/{provincia}/residencia", response_model=List[schemas.Vacuna], tags=["Vacunas solo por provincia de residencia"])
def read_vacunas(provincia: models.ModelProvince, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_residence_provincia(db, provincia, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/provincia/{provincia}/residencia/count", tags=["Vacunas solo por provincia de residencia"])
def read_vacunas(provincia: models.ModelProvince, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_residence_provincia_count(db, provincia)
    return vacunas


# Application province
@app.get("/vacunas/provincia/{provincia}/aplicacion", response_model=List[schemas.Vacuna], tags=["Vacunas solo por provincia donde se aplició la dosis"])
def read_vacunas(provincia: models.ModelProvince, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_aplication_provincia(db, provincia, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/provincia/{provincia}/aplicacion/count", tags=["Vacunas solo por provincia donde se aplició la dosis"])
def read_vacunas(provincia: models.ModelProvince, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_aplication_provincia_count(db, provincia)
    return vacunas


# Vaccine brand/type
@app.get("/vacunas/marca/{marca}", response_model=List[schemas.Vacuna], tags=["Vacunas solo por marca de vacuna suministrada"])
def read_vacunas(marca: models.ModelVacunas, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_marca(db, marca, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/marca/{marca}/count", tags=["Vacunas solo por marca de vacuna suministrada"])
def read_vacunas(marca: models.ModelVacunas, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_marca_count(db, marca)
    return vacunas


# Number of dosis
@app.get("/vacunas/dosis/{dosis}", response_model=List[schemas.Vacuna], tags=["Vacunas solo por número de dosis"])
def read_vacunas(dosis: models.ModelDosis, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_dosis(db, dosis, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/dosis/{dosis}/count", tags=["Vacunas solo por número de dosis"])
def read_vacunas(dosis: models.ModelDosis, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_dosis_count(db, dosis)
    return vacunas


#########################   Double metrics #########################

#### Age - X ####
@app.get("/vacunas/age/{age}/condition/{condition}", response_model=List[schemas.Vacuna], tags=["Vacunas por edad y otro factor"])
def read_vacunas(age: models.ModelAge, condition: models.ModelCondiciones, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_condition(db, age, condition, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/age/{age}/condition/{condition}/count", tags=["Vacunas por edad y otro factor"])
def read_vacunas(age: models.ModelAge, condition: models.ModelCondiciones, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_condition_count(db, age, condition)
    return vacunas


@app.get("/vacunas/age/{age}/provincia/{provincia}", response_model=List[schemas.Vacuna], tags=["Vacunas por edad y otro factor"])
def read_vacunas(age: models.ModelAge, provincia: models.ModelProvince, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_provincia(db, age, provincia, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/age/{age}/provincia/{provincia}/count", tags=["Vacunas por edad y otro factor"])
def read_vacunas(age: models.ModelAge, provincia: models.ModelProvince, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_provincia_count(db, age, provincia)
    return vacunas


@app.get("/vacunas/age/{age}/vacuna/{vacuna}", response_model=List[schemas.Vacuna], tags=["Vacunas por edad y otro factor"])
def read_vacunas(age: models.ModelAge, vacuna: models.ModelVacunas, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_vacuna(db, age, vacuna, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/age/{age}/vacuna/{vacuna}/count", tags=["Vacunas por edad y otro factor"])
def read_vacunas(age: models.ModelAge, vacuna: models.ModelVacunas, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_vacuna_count(db, age, vacuna)
    return vacunas


@app.get("/vacunas/age/{age}/dosis/{dosis}", response_model=List[schemas.Vacuna], tags=["Vacunas por edad y otro factor"])
def read_vacunas(age: models.ModelAge, dosis: models.ModelDosis,  skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_dosis(db, age, dosis, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/age/{age}/dosis/{dosis}/count", tags=["Vacunas por edad y otro factor"])
def read_vacunas(age: models.ModelAge, dosis: models.ModelDosis, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_dosis_count(db, age, dosis)
    return vacunas


#### Type - X ####
@app.get("/vacunas/vacuna/{vacuna}/provincia/{provincia}", response_model=List[schemas.Vacuna], tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(provincia: models.ModelProvince, vacuna: models.ModelVacunas, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_provincia(db, provincia, vacuna, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/vacuna/{vacuna}/provincia/{provincia}/count", tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(provincia: models.ModelProvince, vacuna: models.ModelVacunas, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_provincia_count(db, provincia, vacuna)
    return vacunas


@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}", response_model=List[schemas.Vacuna], tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis: models.ModelDosis, vacuna: models.ModelVacunas, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis(db, dosis, vacuna, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/count", tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis: models.ModelDosis, vacuna: models.ModelVacunas, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_count(db, dosis, vacuna)
    return vacunas


#### Condition - X ####
@app.get("/vacunas/condicion/{condicion}/provincia/{provincia}", response_model=List[schemas.Vacuna], tags=["Vacunas por condición y otro factor"])
def read_vacunas(condicion: models.ModelCondiciones, provincia: models.ModelProvince, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_condicion_provincia(db, condicion, provincia, skip=skip, limit=limit)
    return vacunas


@app.get("/vacunas/condicion/{condicion}/provincia/{provincia}/count", tags=["Vacunas por condición y otro factor"])
def read_vacunas(condicion: models.ModelCondiciones, provincia: models.ModelProvince, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_condicion_provincia_count(db, condicion, provincia)
    return vacunas


@app.get("/vacunas/condicion/{condicion}/dosis/{dosis}", response_model=List[schemas.Vacuna], tags=["Vacunas por condición y otro factor"])
def read_vacunas(condicion: models.ModelCondiciones, dosis: models.ModelDosis, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_condicion_dosis(db, condicion, dosis, skip=skip, limit=limit)
    return vacunas


@app.get("/vacunas/condicion/{condicion}/dosis/{dosis}/count", tags=["Vacunas por condición y otro factor"])
def read_vacunas(condicion: models.ModelCondiciones, dosis: models.ModelDosis, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_condicion_dosis_count(db, condicion, dosis)
    return vacunas


@app.get("/vacunas/condicion/{condicion}/vacuna/{vacuna}", response_model=List[schemas.Vacuna], tags=["Vacunas por condición y otro factor"])
def read_vacunas(condicion: models.ModelCondiciones, vacuna: models.ModelVacunas, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_condicion_vacuna(db, condicion, vacuna, skip=skip, limit=limit)
    return vacunas


@app.get("/vacunas/condicion/{condicion}/vacuna/{vacuna}/count", tags=["Vacunas por condición y otro factor"])
def read_vacunas(condicion: models.ModelCondiciones, vacuna: models.ModelVacunas, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_condicion_vacuna_count(db, condicion, vacuna)
    return vacunas


#### Province - X ####
@app.get("/vacunas/provincia/{provincia}/fecha/{fecha}", response_model=List[schemas.Vacuna], tags=["Vacunas por provincia y otro factor"])
def read_vacunas(provincia: models.ModelProvince, fecha: str = Path(..., description="La fecha está en el formato: 2021-05-03"), skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_provincia_fecha(db, provincia, fecha, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/provincia/{provincia}/fecha/{fecha}/count", tags=["Vacunas por provincia y otro factor"])
def read_vacunas(provincia: models.ModelProvince, fecha: str = Path(..., description="La fecha está en el formato: 2021-05-03"), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_provincia_fecha_count(db, provincia, fecha)
    return vacunas


@app.get("/vacunas/provincia/{provincia}/dosis/{dosis}", response_model=List[schemas.Vacuna], tags=["Vacunas por provincia y otro factor"])
def read_vacunas(provincia: models.ModelProvince, dosis: models.ModelDosis, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_provincia_dosis(db, provincia, dosis, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/provincia/{provincia}/dosis/{dosis}/count", tags=["Vacunas por provincia y otro factor"])
def read_vacunas(provincia: models.ModelProvince, dosis: models.ModelDosis, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_provincia_dosis_count(db, provincia, dosis)
    return vacunas


#########################   Triple metrics #########################
## Vacuna - Dosis - Provincia ##
@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/provincia/{provincia}", response_model=List[schemas.Vacuna], tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis: models.ModelDosis, vacuna: models.ModelVacunas, provincia: models.ModelProvince, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_provincia(db, dosis, vacuna, provincia, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/provincia/{provincia}/count", tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis: models.ModelDosis, vacuna: models.ModelVacunas, provincia=str, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_provincia_count(db, dosis, vacuna, provincia)
    return vacunas


## Vacuna - Dosis - Condicion ###
@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/condition/{condition}", response_model=List[schemas.Vacuna], tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis: models.ModelDosis, vacuna: models.ModelVacunas, condition: models.ModelCondiciones, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_condition(db, dosis, vacuna, condition, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/condition/{condition}/count", tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis: models.ModelDosis, vacuna: models.ModelVacunas, condition: models.ModelCondiciones, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_condition_count(db, dosis, vacuna, condition)
    return vacunas


## Vacuna - Dosis - Edad ##
@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/age/{age}", response_model=List[schemas.Vacuna], tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis: models.ModelDosis, vacuna: models.ModelVacunas, age: models.ModelAge, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_age(db, dosis, vacuna, age, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/age/{age}/count", tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis: models.ModelDosis, vacuna: models.ModelVacunas, age: models.ModelAge, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_age_count(db, dosis, vacuna, age)
    return vacunas


## Vacuna - Provincia - Fecha ##
@app.get("/vacunas/vacuna/{vacuna}/provincia/{provincia}/fecha/{fecha}", response_model=List[schemas.Vacuna], tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(vacuna: models.ModelVacunas, provincia: models.ModelProvince, fecha: str = Path(..., description="La fecha está en el formato: 2021-05-03"), skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_provincia_fecha(db, provincia, vacuna, fecha, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/vacuna/{vacuna}/provincia/{provincia}/fecha/{fecha}/count", tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(vacuna: models.ModelVacunas, provincia: models.ModelProvince, fecha: str = Path(..., description="La fecha está en el formato: 2021-05-03"), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_provincia_fecha_count(db, provincia, vacuna, fecha)
    return vacunas


## Vacuna - Provincia - Dosis - Fecha ##
@app.get("/vacunas/vacuna/{vacuna}/provincia/{provincia}/dosis/{dosis}/fecha/{fecha}", response_model=List[schemas.Vacuna], tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(vacuna: models.ModelVacunas, provincia: models.ModelProvince, dosis: models.ModelDosis, fecha: str = Path(..., description="La fecha está en el formato: 2021-05-03"), skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_provincia_dosis_fecha(db, provincia, vacuna, dosis, fecha, limit=limit, skip=skip)
    return vacunas


@app.get("/vacunas/vacuna/{vacuna}/provincia/{provincia}/dosis/{dosis}/fecha/{fecha}/count", tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(vacuna: models.ModelVacunas, provincia: models.ModelProvince, dosis: models.ModelDosis, fecha: str = Path(..., description="La fecha está en el formato: 2021-05-03"), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_provincia_dosis_fecha_count(db, provincia, vacuna, dosis, fecha)
    return vacunas
