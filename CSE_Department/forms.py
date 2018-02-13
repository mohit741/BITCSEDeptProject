from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )


class RegForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'name',
            'dept',
            'phone',
        )

