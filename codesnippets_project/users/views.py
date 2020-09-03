from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import AnonymousUser
from .models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(to='snippets.html')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def login(request):
    retry = False
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(to='userprofile.html')
        else:
            retry = False
    return render(request, 'login.html', {'retry': retry})
        
        

def logout(request):
    logout(request)
    return render(request, 'snippets.html')
