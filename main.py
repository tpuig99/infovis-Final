from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException,Query, Path
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

############ Endpoints Description #############
tags_metadata = [
    {"name": "General Vacunas", "description": "Obtiene las vacunas sin ningún filtro."},
    {"name": "Vacunas solo por sexo", "description": "Obtiene las vacunas filtradas por sexo."},
    {"name": "Vacunas solo por edad", "description": "Obtiene las vacunas filtradas por grupo etario."},
    {"name": "Vacunas solo por condicion", "description": "Obtiene las vacunas filtradas por la condición de la aplicación."},
    {"name": "Vacunas por provincia y otro factor", "description": "Obtiene las vacunas filtradas por provincia y: fecha."},
    {"name": "Vacunas por edad y otro factor", "description": "Obtiene las vacunas filtradas por grupo etario y: condición de aplicación, provincia, vacuna."},
    {"name": "Vacunas por vacuna y otro factor", "description": "Obtiene las vacunas filtradas por la vacuna y: dosis, provincia, condicion y dosis, provincia y dosis."},
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
@app.get("/vacunas/",response_model=List[schemas.Vacuna],tags=["General Vacunas"])
def read_vacunas(skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    return crud.get_all_vacunas(db,skip=skip, limit=limit)

@app.get("/vacunas/count",tags=["General Vacunas"])
def read_vacunas(db: Session = Depends(get_db)):
    return crud.get_all_vacunas_count(db)
    
@app.get("/vacunas/sex/{sex}",response_model=List[schemas.Vacuna],tags=["Vacunas solo por sexo"])
def read_vacunas(sex:models.ModelSex, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_sex(db,sex,limit=limit,skip=skip)
    return vacunas

@app.get("/vacunas/sex/{sex}/count", tags=["Vacunas solo por sexo"])
def read_vacunas(sex:models.ModelSex, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_sex_count(db,sex)
    return vacunas

@app.get("/vacunas/condition/{condition}",response_model=List[schemas.Vacuna], tags=["Vacunas solo por condicion"])
def read_vacunas(condition:models.ModelCondiciones, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_condition(db,condition,limit=limit,skip=skip)
    return vacunas

@app.get("/vacunas/condition/{condition}/count", tags=["Vacunas solo por condicion"])
def read_vacunas(condition:models.ModelCondiciones, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_condition_count(db,condition)
    return vacunas

@app.get("/vacunas/age/{age}",response_model=List[schemas.Vacuna],tags=["Vacunas solo por edad"])
def read_vacunas(age:models.ModelAge, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age(db,age=age,limit=limit,skip=skip)
    return vacunas

@app.get("/vacunas/age/{age}/count",tags=["Vacunas solo por edad"])
def read_vacunas(age:models.ModelAge, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_sex_count(db,age)
    return vacunas

#########################   Double metrics #########################

#### Age - X ####
@app.get("/vacunas/age/{age}/condition/{condition}",response_model=List[schemas.Vacuna], tags=["Vacunas por edad y otro factor"])
def read_vacunas(age:models.ModelAge, condition:models.ModelCondiciones, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_condition(db,age=age,condition=condition,limit=limit,skip=skip)
    return vacunas

@app.get("/vacunas/age/{age}/condition/{condition}/count",tags=["Vacunas por edad y otro factor"])
def read_vacunas(age:models.ModelAge, condition:models.ModelCondiciones,db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_condition_count(db,age=age,condition=condition)
    return vacunas

@app.get("/vacunas/age/{age}/provincia/{provincia}",response_model=List[schemas.Vacuna],tags=["Vacunas por edad y otro factor"])
def read_vacunas(age:models.ModelAge, provincia:str, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_provincia(db,age=age,provincia=provincia,limit=limit,skip=skip)
    return vacunas

@app.get("/vacunas/age/{age}/provincia/{provincia}/count",tags=["Vacunas por edad y otro factor"])
def read_vacunas(age:models.ModelAge, provincia:str,db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_provincia_count(db,age=age,provincia=provincia)
    return vacunas

@app.get("/vacunas/age/{age}/vacuna/{vacuna}",response_model=List[schemas.Vacuna],tags=["Vacunas por edad y otro factor"])
def read_vacunas(age:models.ModelAge, vacuna:models.ModelVacunas, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_vacuna(db,age=age,vacuna=vacuna,limit=limit,skip=skip)
    return vacunas

@app.get("/vacunas/age/{age}/vacuna/{vacuna}/count",tags=["Vacunas por edad y otro factor"])
def read_vacunas(age:models.ModelAge, vacuna:models.ModelVacunas,db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_age_vacuna_count(db,age=age,vacuna=vacuna)
    return vacunas

#### Type - X ####
@app.get("/vacunas/vacuna/{vacuna}/provincia/{provincia}",response_model=List[schemas.Vacuna],tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(provincia:str, vacuna:models.ModelVacunas, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_provincia(db,provincia=provincia,vacuna=vacuna,limit=limit,skip=skip)
    return vacunas

@app.get("/vacunas/vacuna/{vacuna}/provincia/{provincia}/count",tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(provincia:str, vacuna:models.ModelVacunas,db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_provincia_count(db,provincia=provincia,vacuna=vacuna)
    return vacunas

@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}",response_model=List[schemas.Vacuna],tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis:int, vacuna:models.ModelVacunas, skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis(db,dosis=dosis,vacuna=vacuna,limit=limit,skip=skip)
    return vacunas

@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/count",tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis:int, vacuna:models.ModelVacunas,db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_count(db,dosis=dosis,vacuna=vacuna)
    return vacunas

#### Provincia - X ####
@app.get("/vacunas/provincia/{provincia}/fecha/{fecha}",response_model=List[schemas.Vacuna],tags=["Vacunas por provincia y otro factor"])
def read_vacunas(provincia:str, fecha:str = Path(...,description="La fecha está en el formato: 2021-05-03"), skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_provincia_fecha(db,provincia=provincia,fecha=fecha,limit=limit,skip=skip)
    return vacunas

@app.get("/vacunas/provincia/{provincia}/fecha/{fecha}/count",tags=["Vacunas por provincia y otro factor"])
def read_vacunas(provincia:str, fecha:str = Path(...,description="La fecha está en el formato: 2021-05-03"),db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_provincia_fecha_count(db,provincia=provincia,fecha=fecha)
    return vacunas

#########################   Triple metrics #########################

@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/provincia/{provincia}",response_model=List[schemas.Vacuna],tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis:int, vacuna:models.ModelVacunas, provincia:str,skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_provincia(db,dosis=dosis,vacuna=vacuna,provincia=provincia,limit=limit,skip=skip)
    return vacunas

@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/provincia/{provincia}/count",tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis:int, vacuna:models.ModelVacunas,provincia=str,db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_provincia_count(db,dosis=dosis,vacuna=vacuna,provincia=provincia)
    return vacunas

@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/condition/{condition}",response_model=List[schemas.Vacuna],tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis:int, vacuna:models.ModelVacunas, condition:models.ModelCondiciones,skip: int = 0, limit: Optional[int] = Query(None, description="No es un campo obligatorio, sin embargo por la gran cantidad de datos recomendamos darle uso."), db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_condition(db,dosis=dosis,vacuna=vacuna,condition=condition,limit=limit,skip=skip)
    return vacunas

@app.get("/vacunas/vacuna/{vacuna}/dosis/{dosis}/condition/{condition}/count",tags=["Vacunas por vacuna y otro factor"])
def read_vacunas(dosis:int, vacuna:models.ModelVacunas,condition=str,db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_vacuna_dosis_condition_count(db,dosis=dosis,vacuna=vacuna,condition=condition)
    return vacunas