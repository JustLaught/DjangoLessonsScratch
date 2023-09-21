from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    style = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    avalible = models.BooleanField()
    reader = models.ForeignKey("Reader", related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.author} | {self. year} | {self.style} | {self.publisher} | {self.avalible} | {self.reader}'

class Reader(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    visit_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.name} | {self.lastname} | {self.phone} | {self.email} | {self.visit_date}'