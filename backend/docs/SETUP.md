
### `SETUP.md`
This document provides instructions for setting up the project.

# Setup Instructions

## Prerequisites
- Python 3.x
- Django
- Django REST Framework

## Installation

1. **Clone the Repository**
   
   ```bash
   git clone https://github.com/shyama7004/TaskBee.git
   cd your-repo
   ```
2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   
   ```bash
   python manage.py migrate
    ```

5. **Start the Development Server**

    ```bash
    python manage.py runserver
    ```
