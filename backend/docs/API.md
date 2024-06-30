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
  
### Response
 
 ```json
  {
    "id": 1,
    "title": "Test Task",
    "description": "This is a test task",
    "due_time": "2024-06-30T12:00:00Z",
    "status": "pending",
    "user": 1
  }
```
### List Tasks
- **URL:** `/api/tasks/`
- **Method:**` GET`
- **Response:**
```
[
  {
    "id": 1,
    "title": "Test Task",
    "description": "This is a test task",
    "due_time": "2024-06-30T12:00:00Z",
    "status": "pending",
    "user": 1
  }
]
```
<!--```ruby

#### `backend/docs/SETUP.md`
```markdown
# Setup Guide

## Prerequisites

- Python 3.x
- pip
- Django

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/taskzen.git
    cd taskzen/backend
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations and run the server:**
    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

## Running Tests

To run the tests, use the following command:
```sh
python manage.py test
```
```csharp

#### `backend/docs/ARCHITECTURE.md`
```markdown
# Architecture Overview

## Project Structure

- **backend/**: Contains the Django backend code.
  - **manage.py**: Django's command-line utility.
  - **backend/**: Project settings and configuration.
  - **tasks/**: Application that handles task management.
    - **models.py**: Database models for tasks.
    - **serializers.py**: Serializers to convert model instances to JSON.
    - **views.py**: Views to handle the API endpoints.
    - **tests/**: Contains unit tests for models and views.
  - **docs/**: Contains detailed documentation for the backend.

## Models

### Task
- **Fields:**
  - `user`: ForeignKey to the User model.
  - `title`: CharField to store the task title.
  - `description`: TextField to store the task description.
  - `due_time`: DateTimeField to store the due time of the task.
  - `status`: CharField to store the status of the task (pending, completed, overdue).

## API Endpoints

- **/api/tasks/**: Handles CRUD operations for tasks.
```
-->
