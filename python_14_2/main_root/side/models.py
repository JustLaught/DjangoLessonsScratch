from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(name='name', max_length=50)
    login = models.CharField(name='login', max_length=50, default='')
    password = models.CharField(name='password', max_length=50)
    superuser = models.BooleanField()