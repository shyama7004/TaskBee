# Contributing to TaskBee

First off, thank you for considering contributing to TaskBee! It's people like you that make this project a great place to learn, inspire, and create.

---

## How to Contribute

### 1. Fork the Repository

Fork the repository by clicking the "Fork" button at the top right of the page. This will create a copy of the repository in your GitHub account.

### 2. Clone the Repository

Clone your forked repository to your local machine.

```sh
git clone https://github.com/your-username/TaskBee.git
cd TaskBee
```
### 3. Create a Branch

Create a new branch for your work. It's good practice to give your branch a descriptive name.

```sh
git add .
git commit -m "Add your descriptive commit message here"
```
### 4. Make Changes

Make your changes to the codebase. If you're working on the frontend (Flutter) or backend (Django), make sure to follow the respective project's guidelines and coding standards.

### 5. Commit Changes

Commit your changes with a clear and concise commit message.

```sh
git add .
git commit -m "Add your descriptive commit message here"
```
### 6. Push to Your Fork

Push your changes to your forked repository.

```sh
git push origin feature/your-feature-name
```
### 7. Open a Pull Request

Go to the original repository and open a pull request. Provide a clear and descriptive title and description of your changes. Make sure to reference any relevant issues.

---

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project, you agree to abide by its terms.

## Reporting Issues
If you find any bugs or issues, please report them using GitHub Issues. Provide as much detail as possible, including steps to reproduce the issue and any relevant screenshots.

## Pull Request Guidelines
1. Write clear, concise commit messages: Each commit message should describe the change in detail.
2. Ensure tests pass: Make sure that all tests pass before submitting your pull request.
3. Keep your changes focused: Each pull request should focus on a single feature or bug fix. Avoid combining unrelated changes.
4. Follow the coding standards: Ensure your code follows the project's coding standards and guidelines.
5. Document your changes: Update any relevant documentation to reflect your changes.

---
## Development Setup
### Prerequisites
  [![Flutter](https://img.shields.io/badge/Flutter-Flutter.com-8B0000?style=for-the-badge)](https://flutter.dev/docs/get-started/install)
  [![Django](https://img.shields.io/badge/Django-Django.com-00008B?style=for-the-badge)](https://www.djangoproject.com/download/)
  [![Python](https://img.shields.io/badge/Python-Python.com-013220?style=for-the-badge)](https://www.python.org/downloads/)
  [![pip](https://img.shields.io/badge/pip-pip.com-8B8000?style=for-the-badge)](https://pip.pypa.io/en/stable/installation/)

---

## Backend Setup (Django)
1. Navigate to the backend directory:

```sh
cd backend
```
2. Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the dependencies:

```sh
pip install -r requirements.txt
```
4. Apply migrations and run the server:

```sh
python manage.py migrate
python manage.py runserver
```

---
## Frontend Setup (Flutter)
1. Navigate to the frontend directory:

```sh
cd ../frontend
```
2. Get the Flutter dependencies:

```sh
flutter pub get
```
3. Run the app:

```sh
flutter run
```
---
## Thank You!
Thank you for taking the time to contribute to TaskBee! Your contributions help improve the project and make it more useful for everyone. If you have any questions, feel free to reach out.





