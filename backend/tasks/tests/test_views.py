from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.models import Task
from rest_framework.test import APIClient
from datetime import datetime

class TaskViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = APIClient()
        self.client.login(username='testuser', password='12345')

    def test_task_creation(self):
        url = reverse('task-list')
        data = {
            'title': 'Test Task',
            'description': 'This is a test task',
            'due_time': datetime.now().isoformat(),
            'user': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')
