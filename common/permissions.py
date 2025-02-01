from rest_framework.permissions import BasePermission
from django.conf import settings

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_admin

class IsOperatorUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_operator

    def has_object_permission(self, request, view, obj):
        # Allow GET, POST, PUT, PATCH methods but not DELETE
        if request.method in ['GET', 'POST', 'PUT', 'PATCH']:
            return True
        return False
    
class HasAPIKey(BasePermission):
    def has_permission(self, request, view):
        api_key = request.headers.get('X-API-KEY')
        return api_key == settings.API_KEY