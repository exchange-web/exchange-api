from django.urls import path
from .views import verify_login, me, register, UserByCodeView


urlpatterns = [
    path('login/', verify_login, name='verify_login'),
    path('me/', me, name='me'),
    path('register/', register, name='register'),
    path('/', UserByCodeView.as_view(), name='user_by_code')
]