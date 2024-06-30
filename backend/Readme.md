# TaskBee Backend

Welcome to the backend of TaskBee, a task management application. This project is built using Django and provides RESTful APIs for managing tasks.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```plaintext
TaskBee/
├── backend/
│   ├── manage.py
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_models.py
│   │   │   ├── test_views.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── docs/
│   │   ├── API.md
│   │   ├── SETUP.md
│   │   ├── ARCHITECTURE.md
│   ├── requirements.txt
│   ├── ...
```

### Directories and Files

- **backend/**: Contains the Django project settings and configurations.
  - **manage.py**: Django's command-line utility.
  - **backend/**: Django project directory.
    - **settings.py**: Settings and configuration for the Django project.
    - **urls.py**: URL routing for the project.
    - **wsgi.py**: WSGI application entry point.
- **tasks/**: Django app for task management.
  - **__init__.py**: Initializes the app.
  - **admin.py**: Admin configurations for the app.
  - **apps.py**: App configuration.
  - **models.py**: Database models for the app.
  - **serializers.py**: Serializers for converting complex data types to JSON.
  - **tests/**: Directory containing test cases.
    - **__init__.py**: Initializes the test module.
    - **test_models.py**: Test cases for models.
    - **test_views.py**: Test cases for views.
  - **urls.py**: URL routing for the tasks app.
  - **views.py**: View functions for handling requests.
- **docs/**: Documentation for the project.
  - **API.md**: Detailed API documentation.
  - **SETUP.md**: Instructions for setting up the project.
  - **ARCHITECTURE.md**: Overview of the project's architecture.
- **requirements.txt**: List of dependencies.

## Features

- **Task Management**: Create, update, delete, and retrieve tasks.
- **Task Scheduling**: Set tasks for specific times and get notifications.
- **Task Organization**: Organize tasks into different folders based on their status.
- **User Interaction**: Congratulate users on task completion.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- pip

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shyama7004/TaskBee.git
   cd TaskBee/backend
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## Running the Application

After following the installation steps, you can run the development server:

```bash
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` to access the application.

## API Documentation

For detailed API documentation, refer to [docs/API.md](docs/API.md).

## Testing

To run tests, use the following command:

```bash
python manage.py test
```

This will execute the test cases in the `tasks/tests/` directory.

## Contributing

We welcome contributions! Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for checking out TaskBee! If you have any questions or feedback, feel free to open an issue or contact us at [gmail.com](mailto:sujatabisoyi@gmail.com).
