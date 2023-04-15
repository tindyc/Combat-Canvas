"""HOME URLs"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('arttherapy/', views.artTherapy, name="arttherapy"),
]
