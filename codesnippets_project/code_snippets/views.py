from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser
from .models import Snippet

# Create your views here.
def snippets(request):
    logged_in = False
    if request.user.is_authenticated:
        logged_in = True
    snippets = Snippet.objects.all()
    return render(request, 'snippets.html', {'snippets': snippets, 'logged_in': logged_in})

