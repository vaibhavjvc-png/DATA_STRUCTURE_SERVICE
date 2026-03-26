 rom sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    data_elements = relationship("DataElement", back_populates="dataset")


class DataElement(Base):
    __tablename__ = "data_elements"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    data_type = Column(String, nullable=False)
    is_pii = Column(Boolean, default=False)

    dataset_id = Column(Integer, ForeignKey("datasets.id"))

    dataset = relationship("Dataset", back_populates="data_elements")
