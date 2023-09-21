from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.show_books, name='show_books'),
    path('readers/', views.show_readers, name='show_readers'),
    path('on_hand/<int:id>', views.show_onhand, name='show_onhand'),
]
