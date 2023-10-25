from django.contrib import admin
from .models import Writing, Author

# Register your models here.
admin.site.register([Writing, Author])