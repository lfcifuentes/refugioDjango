from django import forms
from ..pet.models import Pet


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet

        fields = [
            'name',
            'sex',
            'approximated_age',
            'rescue_date',
            'person',
            'vaccine'
        ]

        labels = {
            'name': 'Name',
            'sex': 'Sex',
            'approximated_age': 'Approximated Age',
            'rescue_date': 'Rescue date',
            'person': 'Person',
            'vaccine': 'Vaccine'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.TextInput(attrs={'class': 'form-control'}),
            'approximated_age': forms.TextInput(attrs={'class': 'form-control'}),
            'rescue_date': forms.TextInput(attrs={'class': 'form-control'}),
            'person': forms.Select(attrs={'class': 'form-control'}),
            'vaccine': forms.CheckboxSelectMultiple()
        }