from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('name', max_length=25)
    password = models.CharField('password', max_length=50)
    superuser = models.BooleanField('superuser')

    def __str__(self):
        return f'{self.name}  |  {self.superuser}'