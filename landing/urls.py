from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='index'),
    path('landing/', views.landing, name='index'),
    path('data/<int:pi_id>/', views.data, name='index'),
    path('addDataPoint/<int:pi_id>', views.addDataPoint, name='index'),  # Post data can't be forwarded
    path('addDataPoint/<int:pi_id>/', views.addDataPoint, name='index'),
    path('auth/logout/', views.logout_view, name='logout'),
]
