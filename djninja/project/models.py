from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Base(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Project(Base):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class Column(Base):
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE
    )


class Task(models.Model):
    column = models.ForeignKey(
        Column,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    text = models.CharField(max_length=100)

    