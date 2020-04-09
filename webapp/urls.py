from django.conf.urls import url
from django.urls import include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^hey/', views.index, name='index'),
]