# API Documentation

## Endpoints

### 1. List and Create Tasks
- **URL**: `/tasks/`
- **Method**: `GET`, `POST`
- **Description**: 
  - `GET`: Retrieve a list of all tasks.
  - `POST`: Create a new task.

#### Request Body (POST)
```json
{
  "title": "Task Title",
  "due_time": "HH:MM:SS",
  "completed": false
}
```
#### Response (GET)
```json
[
  {
    "id": 1,
    "title": "Task Title",
    "due_time": "HH:MM:SS",
    "completed": false
  }
]
```

### 2. Retrieve, Update, and Delete a Task

- **URL:** `/tasks/<id>/`
- **Method:** `GET, PUT, DELETE`
- **Description:**
  - `GET`: Retrieve details of a specific task.
  - `PUT`: Update a task.
  - `DELETE`: Delete a task.
  
#### Request Body (PUT)
```json
{
  "title": "Updated Task Title",
  "due_time": "HH:MM:SS",
  "completed": true
}
```


