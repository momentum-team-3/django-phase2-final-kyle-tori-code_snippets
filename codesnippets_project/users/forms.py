from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class NewUserCreationForm(UserCreationForm):
    pass

class ChangeUserForm(UserChangeForm):
    pass

