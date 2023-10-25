from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addrestoran/', views.addrestoran, name='addrestoran'),
    path('showrestorans/', views.showrestorans, name='showrestorans'),
    path('showrestorans/<str:spec>', views.showrestorans, name='showrestorans'),
    path('showrestoran/<int:id>', views.showrestoran, name='showrestoran'),
]
