from django.contrib import admin
from .models import Page

# Register your models here.

# admin.site.register(Page)  =  Колт не редагуємо

@admin.register(Page)  #  =  Коли редагуєм
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date', 'permalink')
    ordering = ('title',)
    search_fields = ('title', 'permalink')