from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('labas/<slug:vardas>', views.graph_view, name='labas'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
]
