from django.urls import path
from .views import home_view, auth_view, verify_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', auth_view, name='login-view'),
    path('verify/', verify_view, name='verify-view'),
]