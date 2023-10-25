from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index2'),
    path('country/<str:name>', views.country, name='country'),
    path('regions/', views.get_region, name='regions'),
    path('region/<str:region>', views.region, name='region'),
    path('capital/<str:capital>', views.get_capital, name='capital'),
    path('lang/<str:lang>', views.get_lang, name='lang'),
    path('languages/', views.languages, name='languages'),
    path('countries_by_lang/<str:lang>', views.countries_by_lang, name='countries_by_lang')
]
