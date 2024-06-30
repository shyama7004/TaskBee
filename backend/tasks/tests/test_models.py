from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task
from datetime import datetime

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='This is a test task',
            due_time=datetime.now()
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task')
        self.assertEqual(self.task.user.username, 'testuser')
