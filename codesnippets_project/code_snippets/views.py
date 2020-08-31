from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect(to='userprofile.html')
        else:
            for err in form.error_messages:
                print(form.error_messages[err])
            return render(request, 'register.html', {'form': form})

    form = UserCreationForm()
    # return

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(to='userprofile.html')
    else:
        return redirect(to='login.html')

def userprofile(request):
    if not request.user.is_authenticated:
        return render(request, 'login_error.html')