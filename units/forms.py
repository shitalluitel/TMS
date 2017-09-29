from django import forms
from .models import Unit


class UnitForm(forms.ModelForm):

    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kilogram'}),
    )

    print_name = forms.CharField(
        label='Print Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kg'})
    )

    class Meta:
        model = Unit
        fields = {'name', 'print_name'}