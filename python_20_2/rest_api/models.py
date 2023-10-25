from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('Name', max_length=25)

    def __str__(self):
        return f'{self.name}'
    

class Writing(models.Model):
    writing = models.TextField('writing')
    type = models.CharField('type', max_length=10)
    writer = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='witer')

    def __str__(self) -> str:
        return f'{self.writer} : {self.type} : {self.writing}'