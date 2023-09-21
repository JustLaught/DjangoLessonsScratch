from django.db import models

# Create your models here.

class PhoneBook(models.Model):
    name = models.CharField('Name', max_length=30)
    lastname = models.CharField('LastName', max_length=30)
    email = models.EmailField('Email', max_length=254)
    phone = models.CharField('Phone', max_length=18)
    about = models.CharField('About', max_length=150)

    def __str__(self):
        return f"'ID': {self.id} | 'name': {self.name} | 'lastname': {self.lastname} | 'email': {self.email}, 'phone': {self.phone} | 'about': {self.about}"