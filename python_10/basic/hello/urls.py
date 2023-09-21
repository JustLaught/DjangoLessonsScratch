from django.urls import path
from . import views


# www.site.com = ""
# www.site.com/admin = "admin/"
# www.article/article = "article/"

urlpatterns = [
    path("", views.index),
    path("dayofweek", views.day_of_the_week),
    path("cit", views.random_citation),
    path("multi", views.math_scale),
    path("prog_day", views.day_256)
    ]