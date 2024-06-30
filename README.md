<p align="center">
  <img src="https://github.com/shyama7004/TaskBee/blob/main/abstract-origami-triangle-672ld.png" alt="TaskBee Logo" width="200" height="200">
</p>

<h1 align="center">TaskBee</h1>

<p align="center">
  TaskBee is a task management app built with Flutter and Django, designed to help you manage your daily tasks effortlessly. Set tasks, get reminders, track completion, and celebrate your achievements!
</p>

<p align="center">
  <a href="#Features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="https://github.com/shyama7004/AudioZen/blob/main/CONTRIBUTING.md">Contributing</a> •
  <a href="#license">License</a> •
  <a href="#contact">Contact</a>
</p>

---


## 📲 Features

- **Daily Task Setting:** Create tasks for yourself each day.
- **Timed Reminders:** Get notified when it's time to complete your tasks.
- **Task Organization:** Automatically move incomplete tasks to a different folder.
- **Celebration Alerts:** Receive congratulations on task completion.

<!--## 📱 Screenshots

<img src="link-to-screenshot1.png" width="200" alt="Home Screen"> <img src="link-to-screenshot2.png" width="200" alt="Task List"> <img src="link-to-screenshot3.png" width="200" alt="Notifications">
-->

## 🚀 Getting Started

### Prerequisites

  [![Flutter](https://img.shields.io/badge/Flutter-Flutter.com-8B0000?style=for-the-badge)](https://flutter.dev/docs/get-started/install)
  [![Django](https://img.shields.io/badge/Django-Django.com-00008B?style=for-the-badge)](https://www.djangoproject.com/download/)
  [![Python](https://img.shields.io/badge/Python-Python.com-013220?style=for-the-badge)](https://www.python.org/downloads/)
  [![pip](https://img.shields.io/badge/pip-pip.com-8B8000?style=for-the-badge)](https://pip.pypa.io/en/stable/installation/)


### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/TaskBee.git
    cd TaskBee
    ```

2. **Backend Setup (Django):**
    ```sh
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

3. **Frontend Setup (Flutter):**
    ```sh
    cd ../frontend
    flutter pub get
    flutter run
    ```

## 📚 Usage

1. **Create Tasks:** Open the app and set tasks for yourself by providing the task title, description, and due time.
2. **Receive Notifications:** Get timely reminders for your tasks.
3. **Complete Tasks:** Mark tasks as completed to receive a congratulatory message.
4. **Organize Tasks:** Incomplete tasks will be moved to a separate folder for you to review and manage.

## 📦 Project Structure

```plaintext
TaskBee/
│
├── backend/          # Django backend
│   ├── manage.py
│   ├── backend/
│   ├── tasks/
│   └── requirements.txt
│
└── frontend/         # Flutter frontend
    ├── lib/
    ├── test/
    └── pubspec.yaml
```
## 🌟 Features in Development
**Advanced Task Filtering:** Filter tasks by priority and categories.
**Sync Across Devices:** Sync tasks and progress across multiple devices.
**Dark Mode:** Switch to a dark theme for better usability at night.
## 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project.
2. Create your Feature Branch.
```
git checkout -b feature/AmazingFeature
```
3. Commit your Changes.
```
git commit -m 'Add some AmazingFeature'
```

4. Push to the Branch.
```
git push origin feature/AmazingFeature
```
5. Open a Pull Request.
## 📜 License
Distributed under the [MIT License](https://github.com/shyama7004/TaskBee/blob/main/LICENSE). See [LICENSE](https://github.com/shyama7004/TaskBee/blob/main/LICENSE) for more information.

## 📧 Contact
[![Mail](https://img.shields.io/badge/Mail-sujatabisoyi@gmail.com-6b5b95?style=for-the-badge)](sujatabisoyi@gmail.com)

[![Project Link](https://img.shields.io/badge/Project_Link:-https://github.com/shyama7004/TaskBee-6b5b95?style=for-the-badge)](https://github.com/shyama7004/taskzen)


## 🙏 Acknowledgements
[Flutter](https://flutter.dev/?gad_source=1&gclid=CjwKCAjwhIS0BhBqEiwADAUhc_x_88SXjaFE7llpmPimwziDez_BEtvUEAUuvraQC7xcbpqp48Cp6xoCPd0QAvD_BwE&gclsrc=aw.ds)<br>
[Django](https://www.djangoproject.com/)<br>
Open Source Contributors
