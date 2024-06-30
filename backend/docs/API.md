# API Documentation

## Endpoints

### Create Task
- **URL:** `/api/tasks/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "title": "Test Task",
    "description": "This is a test task",
    "due_time": "2024-06-30T12:00:00Z",
    "user": 1
  }
  
## Response
 
 ```json
  {
    "id": 1,
    "title": "Test Task",
    "description": "This is a test task",
    "due_time": "2024-06-30T12:00:00Z",
    "status": "pending",
    "user": 1
  }
