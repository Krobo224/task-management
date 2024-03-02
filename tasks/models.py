from django.db import models

class User(models.Model):
    """User table
    """
    id = models.AutoField(primary_key=True, unique=True, max_length=10)
    user_name = models.CharField(max_length=100)

class Task(models.Model):
    """Task table
    """

    id = models.CharField(primary_key=True, unique=True, auto_created=True, max_length=10)
    description = models.TextField()
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
