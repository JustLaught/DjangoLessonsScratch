from django.urls import path
from . import views

urlpatterns = [
    path('<int:article_num>/<str:author>', views.index),
    path('<int:article_num>/', views.index),
]