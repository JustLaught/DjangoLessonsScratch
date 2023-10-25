from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registerrewiev/', views.review, name='registerform'),
    path('registersite/', views.sitereview, name='sitereview')
]