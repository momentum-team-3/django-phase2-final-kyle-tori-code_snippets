from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Snippet
from django.http import HttpResponse

# Create your views here.
def snippets(request):
    print('Hello World')
    snippets = Snippet.objects.all()
    return render(request, 'snippets.html', {'snippits': snippets})

# def userprofile(request):
#     if not request.user.is_authenticated:
#         return render(request, 'login_error.html')