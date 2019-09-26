# log/forms.py
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django import forms

# If you don't do this you cannot use Bootstrap CSS


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder': 'Enter your Username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type':'password', 'placeholder': 'Enter your Username'}))

