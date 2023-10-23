from typing import Any
from django.test import TestCase
from .models import Task

# Create your tests here.


class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="first task", body="a body here", ended_at="2021-10-10 10:10:10"
        )

    def test_task_content(self):
        self.assertEqual(self.task.title, "first task")
        self.assertEqual(self.task.body, "a body here")
        self.assertEqual(self.task.ended_at, "2021-10-10 10:10:10")
