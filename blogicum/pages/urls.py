from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('rules/', views.rules)
]
