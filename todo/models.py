from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.TextField(max_length=200)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
