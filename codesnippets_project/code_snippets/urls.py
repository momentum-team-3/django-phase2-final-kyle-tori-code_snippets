from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.snippets, name='snippets'),
    path('<int:pk>/', views.userprofile, name='userprofile'),
    
]
