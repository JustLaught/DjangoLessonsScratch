from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addphone/', views.add_phone, name='add_phone'),
    path('contact/', views.show_contact, name='show_contact'),
    path('contact/<int:id>', views.contact, name='contact'),
    path('delete_contact/<int:id>', views.delete_contact, name='delete_contact'),
    path('serch/', views.serch, name='serch'),
]
