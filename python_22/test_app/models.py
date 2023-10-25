from django.db import models

# Create your models here.

class Task(models.Model):
    action = models.CharField(max_length=300)
    creation_time = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    responsible = models.CharField(max_length=200)