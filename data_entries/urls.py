from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataEntryViewSet

router = DefaultRouter()
router.register(r'data_entries', DataEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]