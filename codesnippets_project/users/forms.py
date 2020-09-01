from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from .models import User

class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

class ChangeUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

