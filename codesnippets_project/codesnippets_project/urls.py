"""codesnippets_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from code_snippets.views import snippets

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('code_snippets.urls')),
    path('', snippets, name='snippets'),

    # path('', snippet_views.snippets_list, name='snippets_list'),
    # path('register/', user_views.register, name='register'),
    # path('login/', user_views.login, name='login'),
    # path('user/', include('code_snippets.urls')),
]
