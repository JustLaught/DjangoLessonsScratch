from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.IndexView.as_view(), name='index2'),
    path('template/', TemplateView.as_view(template_name='test.html'), name='template_view'),
    path('tasks/', views.TaskView.as_view(), name='tasks'),
    path('add_task/', views.AddTaskView.as_view(), name='add_task'),
]
