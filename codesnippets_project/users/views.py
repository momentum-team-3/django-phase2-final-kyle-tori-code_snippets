from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from .forms import NewUserCreationForm, ChangeUserForm
from code_snippets.models import Snippet
from .models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect(to='snippets')
    else:
        form = NewUserCreationForm()
        if form.is_valid():
            form.save()
            return redirect(to='snippets')

    return render(request, 'register.html', {'form': form, 'message': messages})

def login_user(request):
    retry = False
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(to='userprofile')
        else:
            retry = True
    return render(request, 'login_user.html', {'retry': retry})

def logout_user(request):
    logout(request)
    return render(request, 'logout_user.html')


def userprofile(request, pk):
    if not request.user.is_authenticated:
        return redirect(to='login_user')
    user = User.objects.get(pk=pk)
    snippets = Snippet.objects.filter(user=user)
    return render(request, 'userprofile.html', {'user': user, 'snippets': snippets})
