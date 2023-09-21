from django.urls import path
from . import views


app_name = 'new_app'
urlpatterns = [
    path('form/', views.index, name='index'),
    path('thank_you/', views.second_page, name='thank_you_site'),
]