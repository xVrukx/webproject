from django.urls import path
from register.views import *

urlpatterns = [
    path('',register,name='register'),
]