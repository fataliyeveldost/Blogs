from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from.models import CustomUser


class UserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('username','first_name','last_name','email')




class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password"
            }
        )
    )