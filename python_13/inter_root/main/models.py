from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField('Title', max_length=60)
    permalink = models.CharField('Permalink', max_length=24, unique=True)
    bodytext = models.TextField('Page content', blank=True)
    update_date = models.DateTimeField('Last time updated')
    
    def __str__(self) -> str:
        return f"{self.title}"