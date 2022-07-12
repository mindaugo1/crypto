from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")), 


from django.urls import path
from django.contrib.auth import views as auth_views

from main import views as crypto_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crypto_views.home, name='home'),
    path('register/', crypto_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
]
