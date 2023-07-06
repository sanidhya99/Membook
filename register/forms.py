from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.conf import settings
from .manage import UserManager


class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    # username=None
    name=forms.CharField(max_length=20)
    age=forms.CharField(max_length=20)
    number=forms.CharField(max_length=12)
    gender=forms.CharField(max_length=10)
    about=forms.CharField(max_length=100)
    pic=forms.CharField(max_length=2000)
    class Meta:
        model=get_user_model()
        fields=("email","name","age","number","pic","password1","password2","gender","about")


    