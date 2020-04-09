from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.login, name='index'),
    path('landing/', views.landing, name='index'),
    path('data/<int:pi_id>/', views.data, name='index'),
]