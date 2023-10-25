from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('film/<str:title>', views.film, name='film'),
    path('heros/', views.heros, name='heros'),
    path('hero/<str:title>', views.hero, name='hero'),
    path('planets/', views.planets, name='planets'),
    path('planet/<str:title>', views.planet, name='planet'),
    path('ships/', views.ships, name='ships'),
    path('ship/<str:title>', views.ship, name='ship'),
]
