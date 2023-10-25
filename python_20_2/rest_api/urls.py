from django.urls import path
from . import views


urlpatterns = [
    path('predict/', views.index, name='index'),
    path('randnumber/', views.randomnumber, name='randomnumber'),
    path('writing/', views.writing, name='write')
]
