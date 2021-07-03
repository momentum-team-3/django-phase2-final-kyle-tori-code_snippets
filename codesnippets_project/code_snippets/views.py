from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser
from .models import Snippet
from .forms import SearchForm

# Create your views here.
def snippets(request):
    logged_in = False
    if request.user.is_authenticated:
        logged_in = True
    snippets = Snippet.objects.all()
    return render(request, 'snippets.html', {'snippets': snippets, 'logged_in': logged_in})

def search_snippet(request):
    if request.method == "GET":
        form = SearchForm()
        return render(request, 'search.html', {'form': form})
    else:
        title_search = request.POST['title']
        title_search_by = request.POST['title_search_by']
        text_search = request.POST['text']
        text_search_by = request.POST['text_search_by']
        language_search = request.POST['language']
        language_search_by = request.POST['language_search_by']
        


