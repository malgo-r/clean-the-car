import factory
from django.db import models as django_models

from todo.models import Todo


class TodoFactory(factory.Factory):
    class Meta:
        model = Todo

    title = "Sample todo title"
    comment = "Sample comment"
    created = django_models.DateField(auto_now_add=True)
