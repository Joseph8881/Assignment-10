from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth_view),
    path('devices/', views.devices_view),
    path('interfaces/', views.interfaces_view),
]