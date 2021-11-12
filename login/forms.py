from django import forms
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import PasswordInput, Textarea
from .models import Login, Register

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['username','password']
        widgets={
            'password':PasswordInput()
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['username','password','repeatpassword']
        widgets={
            'password':PasswordInput(),
            'repeatpassword':PasswordInput()
        }
