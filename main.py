from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

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

@app.get("/vacunas/",response_model=List[schemas.Vacuna])
def read_vacunas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vacunas = crud.get_all_vacunas(db, skip=skip, limit=limit)
    return vacunas

@app.get("/vacunas/{sex}",response_model=List[schemas.Vacuna])
def read_vacunas(sex:str, db: Session = Depends(get_db)):
    vacunas = crud.get_vacuna_by_sex(db,sex)
    return vacunas