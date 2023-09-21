from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('404page/', views.notfoundpage, name='404page'),
]
