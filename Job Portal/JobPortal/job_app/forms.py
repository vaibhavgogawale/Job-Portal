from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ITjobs


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddITJobs(forms.ModelForm):
    class Meta:
        model = ITjobs
        fields = '__all__'


class UpdateITJobs(forms.ModelForm):
    class Meta:
        model = ITjobs
        fields = '__all__'


