from pydantic import BaseModel
from typing import List

class DataElementBase(BaseModel):
    name: str
    data_type: str
    is_pii: bool = False


class DataElementCreate(DataElementBase):
    pass


class DataElementResponse(DataElementBase):
    id: int

    class Config:
        from_attributes = True


class DatasetBase(BaseModel):
    name: str


class DatasetCreate(DatasetBase):
    pass


class DatasetResponse(DatasetBase):
    id: int
    data_elements: List[DataElementResponse] = []

    class Config:
        from_attributes = True