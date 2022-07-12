from django.urls import path
from .views import HomePageView, AboutPageView, LoginPageView, LogedinPageView



urlpatterns = [
    path("logedin/", LogedinPageView.as_view(), name="logedin"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),

]



"""
from .views import homePageView
urlpatterns = [
    path("", homePageView, name="home"),
]

"""


