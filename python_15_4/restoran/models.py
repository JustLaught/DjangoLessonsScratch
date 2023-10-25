from django.db import models

# Create your models here.


class Restoran(models.Model):
    name = models.CharField('name', max_length=50)
    spec = models.CharField('spec', max_length=50)
    address = models.CharField('address', max_length=70)
    web_site = models.CharField('website', max_length=70)
    phone = models.CharField('phone', max_length=50)

    def __str__(self):
        return f"{self.name}  |  {self.spec}  |  {self.address}  |  {self.web_site}  |  {self.phone}"