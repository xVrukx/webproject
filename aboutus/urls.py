from django.urls import path
from aboutus.views import *

urlpatterns =[
    path('',aboutus,name='aboutus'),
]