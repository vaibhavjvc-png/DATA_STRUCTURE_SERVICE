## Data Model

The service manages an in-memory representation of items.

### Entity: Item
- **id**: Integer (Primary Key, auto-incremented)
- **name**: String (must be unique)
- **value**: Integer (must be greater than 0)

### Relationships
- No relationships (single entity system)

### Design Decisions
- In-memory list is used for storage
- No external database dependency

- ## ⚖️ Assumptions & Trade-offs

### Assumptions
- Application runs on a single instance
- Data is not required to persist after restart
- Users send valid JSON input

### Trade-offs

| Decision | Benefit | Trade-off |
|----------|--------|----------|
| In-memory storage | Fast, simple | No persistence |
| No database | Easy setup | Not scalable |
| Validation in code | Flexible | Slight performance overhead |


## 🧪 Testing Requirements

### Business Rules Enforced

1. Item value must be greater than 0
2. Item name must be unique

### Test Cases

#### Valid Case
Input:
{
  "name": "item1",
  "value": 10
}
Expected: Success

####  Invalid Value
Input:
{
  "name": "item2",
  "value": -5
}
Expected: Error (value must be > 0)

####  Duplicate Name
Input:
{
  "name": "item1",
  "value": 20
}
Expected: Error (name must be unique)

### Enforcement Location
- Value validation → Schema layer
- Unique name → Service layer
