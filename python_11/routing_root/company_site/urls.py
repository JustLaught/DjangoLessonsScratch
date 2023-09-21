from django.urls import path
from . import views


app_name = 'c_site'
urlpatterns = [
    path('branches/<str:name>/', views.branches, name='branches_page'),
    path('branches/<path:name>/', views.branches, name='branches_page'),
    path('branches/', views.branches, name='branches_page'),
    path('news/<path:aftertext>/', views.news, name="news_page"),
    path('news/', views.news, name="news_page"),
    path('managment/<path:aftertext>', views.managment, name="managment_page"),
    path('managment/', views.managment, name="managment_page"),
    path('about/<path:aftertext>', views.about, name="about_page"),
    path('about/', views.about, name="about_page"),
    path('contacts/<path:aftertext>', views.contacts, name="contacts_page"),
    path('contacts/', views.contacts, name="contacts_page"),
    path('', views.index, name="index_page"),
    path('<path:aftertext>', views.index, name="index_page")
]