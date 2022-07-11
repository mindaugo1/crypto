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


