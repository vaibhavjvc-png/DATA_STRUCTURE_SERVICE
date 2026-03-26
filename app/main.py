from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dataset APIs
@app.post("/datasets/", response_model=schemas.DatasetResponse)
def create_dataset(dataset: schemas.DatasetCreate, db: Session = Depends(get_db)):
    return crud.create_dataset(db, dataset)


@app.get("/datasets/", response_model=list[schemas.DatasetResponse])
def list_datasets(db: Session = Depends(get_db)):
    return crud.get_datasets(db)


@app.get("/datasets/{dataset_id}", response_model=schemas.DatasetResponse)
def get_dataset(dataset_id: int, db: Session = Depends(get_db)):
    dataset = crud.get_dataset(db, dataset_id)
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return dataset


# Data Elements APIs
@app.post("/datasets/{dataset_id}/elements/", response_model=schemas.DataElementResponse)
def add_data_element(dataset_id: int, element: schemas.DataElementCreate, db: Session = Depends(get_db)):
    dataset = crud.get_dataset(db, dataset_id)
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")

    return crud.create_data_element(db, dataset_id, element)


@app.get("/datasets/{dataset_id}/elements/", response_model=list[schemas.DataElementResponse])
def list_elements(dataset_id: int, db: Session = Depends(get_db)):
    return crud.get_data_elements(db, dataset_id)

@app.post("/datasets/", response_model=schemas.DatasetResponse)
def create_dataset(dataset: schemas.DatasetCreate, db: Session = Depends(get_db)):
    existing = crud.get_datasets(db)
    
    for d in existing:
        if d.name == dataset.name:
            raise HTTPException(status_code=400, detail="Dataset already exists")

    return crud.create_dataset(db, dataset)
