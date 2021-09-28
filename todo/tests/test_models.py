import pytest
import datetime
from django.db import models


@pytest.mark.django_db
def test_string_representation(todo):
    assert str(todo) == "Sample todo title"


def test_todo_model_creation(todo):
    assert todo.title == "Sample todo title"
    assert todo.comment == "Sample comment"
    assert todo.created == datetime.datetime.now()
