from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shital Luitel'}),
        required=False,
    )

    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Biratnagar-04'}),
        required= False,
    )

    phone_number = forms.CharField(
        label='Phone no.',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '9842574872'}),
        required= False,
    )

    class Meta():
        model = Customer
        fields = {
            'name',
            'address',
            'phone_number',
        }
