from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def snippets(request):
    return render(request, 'snippets.html')

# def userprofile(request):
#     if not request.user.is_authenticated:
#         return render(request, 'login_error.html')