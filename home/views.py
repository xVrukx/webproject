from django.shortcuts import render
from register import *

def home(request):
    user = request.session.get('user', 'Guest')  # default if not set
    return render(request, 'home.html', {'user': user})

