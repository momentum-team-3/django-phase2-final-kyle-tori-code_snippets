from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.snippets, name='snippets'),
    path('search/', views.search_snippet, name='search_snippet')
]
