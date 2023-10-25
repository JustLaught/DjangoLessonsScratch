from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.test, name='test'),
    path('uuid/', views.uuid, name='uuid'),
    path('time/', views.timeOnServer, name='time'),
    path('greettime/', views.greetTime, name='greettime'),
    path('mult2/', views.multiply2, name='multiply2'),
    path('mult/<int:a>/<int:b>', views.multiply, name='multiply'),
    path('add/', views.adding, name='adding'),
    path('mid/', views.midle, name='midle'),
    path('min/', views.minimum, name='minimum'),
    path('max/', views.maximum, name='maximum'),
    path('pow/', views.to_power, name='to_power'),
]
