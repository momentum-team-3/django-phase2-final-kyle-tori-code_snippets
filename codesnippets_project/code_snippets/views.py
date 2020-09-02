from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.forms import UserCreationForm
from .models import Snippet
from users.models import User
from django.http import HttpResponse

# Create your views here.
def snippets(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippets.html', {'snippets': snippets})

def userprofile(request, pk):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    user = User.objects.get(pk=pk)
    if request.user is isinstance(user, AnonymousUser):
        return render(request, 'login.html')
    else:
        snippets = Snippet.objects.filter(user=user)
        return render(request, 'userprofile.html', {'user': user, 'snippets': snippets})