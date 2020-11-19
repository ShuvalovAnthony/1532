from django.urls import path
from .views import *

urlpatterns = [
    path('reg', user_register, name='register'),
    path('log', user_login, name='login'),
    path('logut', user_logout, name='logout'),
    path('lk', lk, name='lk'),
]