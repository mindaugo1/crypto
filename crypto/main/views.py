from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

from django.shortcuts import render

# Create your views here.


#LE
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

class LogedinPageView(TemplateView):
    template_name = "logedin.html"


'''
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello, World!")

'''
