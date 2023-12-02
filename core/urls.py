# urls.py
from django.urls import path
from .views import create_user, login_step1, login_step2

urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('login_step1/', login_step1, name='login_step1'),
    path('login_step2/', login_step2, name='login_step2'),
    # Add other URL patterns as needed
]
