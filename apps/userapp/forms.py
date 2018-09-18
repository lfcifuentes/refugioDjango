from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class registrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

        labels = {
            'username':'User Name',
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'E-mail',
            'password1':'Password1',
            'password2':'Password2'
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'})
        }
