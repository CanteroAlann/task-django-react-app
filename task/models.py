from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,related_name="tasks", null=False)

    def __str__(self):
        return self.title
