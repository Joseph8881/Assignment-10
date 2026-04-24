from django.urls import path, include

urlpatterns = [
    path('', include('dnac.urls')),
]