from django import forms
from .models import Customer


# from django.core.exceptions import  ValidationError

class CustomerForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shital Luitel'}),
    )

    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Biratnagar-04'}),
    )

    phone_number = forms.CharField(
        label='Phone no.',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '9842574872'}),
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.title()

    class Meta():
        model = Customer
        fields = {
            'name',
            'address',
            'phone_number',
        }

        # def clean(self):
        #     cleaned_data = super(CustomerForm, self).clean()
        #     name = cleaned_data.get('name')
        #     phone_number = cleaned_data.get('phone_number')
        #     if Customer.objects.filter(name=name,phone_number=phone_number).exists():
        #         raise ValidationError("Customer with this Name and Phone number already exists.")
