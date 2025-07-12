from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.timezone import now
from .models import Userinfo

def register(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')


        new_user = Userinfo.objects.create(
            user_name=name,
            user_email=email,
            user_number=phone
        )
        new_user.save()
        
        context = {
            'name':name,
            'email':email,
            'phone':phone
        }

        html_message = render_to_string("email.html", context)

        email = EmailMessage(
            subject='🎓 Your Form Details - Django App',
            body=html_message,
            from_email='developeryuvrajsirganor@gmail.com',
            to=[email],
        )
        email.content_subtype = "html"
        email.send()
        request.session['user'] = name

        return redirect('home')

    return render(request, 'register.html')  # Renders form on GET request
