from django import forms
from ..adoption.models import Person, Request


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = [
            'name',
            'last_name',
            'age',
            'phone',
            'email',
            'home'
        ]
        labels = {
            'name': 'Name:',
            'last_name': 'Last Name:',
            'age': 'Age:',
            'phone': 'Phone:',
            'Email': 'Email:',
            'home': 'Home:',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'home': forms.Textarea(attrs={'class': 'form-control'}),
        }


class RequestForm(forms.ModelForm):

    class Meta:
        model = Request

        fields = [
            'number_pet',
            'reasons'
        ]

        labels = {
            'number_pet': 'Number Pet:',
            'reasons': 'Reasons:',
        }

        widgets = {
            'number_pet': forms.TextInput(attrs={'class': 'form-control'}),
            'reasons': forms.Textarea(attrs={'class': 'form-control'}),
        }