from sqlalchemy.orm import Session
from . import models, schemas


def create_dataset(db: Session, dataset: schemas.DatasetCreate):
    db_dataset = models.Dataset(name=dataset.name)
    db.add(db_dataset)
    db.commit()
    db.refresh(db_dataset)
    return db_dataset


def get_datasets(db: Session):
    return db.query(models.Dataset).all()


def get_dataset(db: Session, dataset_id: int):
    return db.query(models.Dataset).filter(models.Dataset.id == dataset_id).first()


def create_data_element(db: Session, dataset_id: int, element: schemas.DataElementCreate):
    db_element = models.DataElement(**element.dict(), dataset_id=dataset_id)
    db.add(db_element)
    db.commit()
    db.refresh(db_element)
    return db_element




def get_data_elements(db: Session, dataset_id: int):
    return db.query(models.DataElement).filter(
        models.DataElement.dataset_id == dataset_id
    ).all()

def create_data_element(db, dataset_id, element):
    existing = db.query(models.DataElement).filter(
        models.DataElement.dataset_id == dataset_id,
        models.DataElement.name == element.name
    ).first()

    if existing:
        raise Exception("Data element already exists")

    db_element = models.DataElement(**element.dict(), dataset_id=dataset_id)
    db.add(db_element)
    db.commit()
    db.refresh(db_element)
    return db_element
