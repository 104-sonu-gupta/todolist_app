from django.contrib import messages
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .forms import CustomRegistrationForm
# Create your views here.

def register(request):
    if request.method=="POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New user account created successfully. Login to Get Started !")
            return redirect('login')
        else:
            messages.error(request, "Validation Error")
        return redirect('register')
        

    else:
        register_form = CustomRegistrationForm()
        content = {
            'register_form' : register_form,
            'title' : 'Registration'
        }
        return render(request, 'register.html', content)