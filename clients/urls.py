# myapp/urls.py

from django.urls import path
from .views import ClientListCreate

urlpatterns = [
    path('clients/', ClientListCreate.as_view(), name='client-list-create'),
]