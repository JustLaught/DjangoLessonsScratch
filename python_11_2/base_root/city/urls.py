from django.urls import path
from . import views


app_name = "city_adv"
urlpatterns = [
    path('news/', views.news, name='news'),
    path('news/<path:aftertex>', views.news, name='news'),
    path('vilage-leaders/', views.vilage_liders, name='vilage-leaders'),
    path('vilage-leaders/<path:aftertex>', views.vilage_liders, name='vilage-leaders'),
    path('fact-no-cap/', views.fact_no_cap, name='fact-no-cap'),
    path('fact-no-cap/<path:aftertex>', views.fact_no_cap, name='fact-no-cap'),
    path('emergency-numbers/', views.emergency_numbers, name='emergency-numbers'),
    path('emergency-numbers/<path:aftertex>', views.emergency_numbers, name='emergency-numbers'),
    path('history/', views.history_site, name='history'),
    path('history/<str:name>', views.history_site, name='history'),
    # path('history/<path:aftertex>', views.history_site, name='history'),
    path('', views.index, name='index'),
    path('<path:aftertext>', views.index, name='index')
]