from django.urls import path
from . import views


urlpatterns = [
    path('', views.time, name='index'),
    path('<str:text>', views.keke, name='index'),
]
