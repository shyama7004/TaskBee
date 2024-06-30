<div class="centered-text">
    # 📝 TaskZen
</div>


<div class="grid-container">
    <img src="https://www.logodesign.net/logo/abstract-origami-triangle-672ld.png?nwm=1&nws=1&industry=All&sf=&txt_keyword=IT" alt="Centered Image">
</div>



TaskZen is a task management app built with Flutter and Django, designed to help you manage your daily tasks effortlessly. Set tasks, get reminders, track completion, and celebrate your achievements!

## 📲 Features

- **Daily Task Setting:** Create tasks for yourself each day.
- **Timed Reminders:** Get notified when it's time to complete your tasks.
- **Task Organization:** Automatically move incomplete tasks to a different folder.
- **Celebration Alerts:** Receive congratulations on task completion.

## 📱 Screenshots

<img src="link-to-screenshot1.png" width="200" alt="Home Screen"> <img src="link-to-screenshot2.png" width="200" alt="Task List"> <img src="link-to-screenshot3.png" width="200" alt="Notifications">

## 🚀 Getting Started

### Prerequisites

- [Flutter](https://flutter.dev/docs/get-started/install)
- [Django](https://www.djangoproject.com/download/)
- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/taskzen.git
    cd taskzen
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
taskzen/
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
