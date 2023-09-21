"""
URL configuration for basic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("hello.urls")),
    path("multi/", include("hello.urls")),
    path("prog_day/", include("hello.urls")),
    path("dayofweek/", include("hello.urls")),
    path("cit/", include("hello.urls")),
    path("europe/", include("europe.urls"))
    # path("cart/", include("hello.urls")),
    # path("catalog/", include("hello.urls"))
]

# www.site.com/cart/add
# www.site.com/cart/delete
# www.site.com/cart/view