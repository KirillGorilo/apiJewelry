from django.contrib import admin
from django.urls import path, include
from base import views
from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.urls')),
]
