from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus/', include('aboutus.urls')),
    path('', include('register.urls')),
    path('home/',include('home.urls')),
]
