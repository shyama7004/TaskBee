# This file contains the database models for your app.

# models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    due_time = models.TimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
