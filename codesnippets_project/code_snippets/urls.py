from django.contrib import admin
from django.urls import path, include
from .views import snippets

urlpatterns = [
    path('', snippets, name='snippets')
]
