# Data Structure Management Service

## Design Decisions
- One-to-many relationship:
  Dataset → DataElements
- Dataset name is unique
- DataElement includes:
  - name
  - data_type
  - is_pii (optional enhancement)

## Constraints
- Dataset name must be unique
- DataElement must belong to a dataset

## Run Project

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload