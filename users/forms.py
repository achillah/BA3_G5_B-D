from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.models import Request
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#register username, email, password1, password2
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#update profile picture (image)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
