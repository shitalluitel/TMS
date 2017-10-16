from django import forms
from items.models import Item
from .models import Transaction
from customers.models import Customer
from django.core.exceptions import ValidationError


class TransactionForm(forms.ModelForm):
    item = forms.ModelChoiceField(
        label='Item Name',
        queryset=Item.objects.all(),
        empty_label='Select Item',
        widget=forms.Select(attrs={'class': 'form-control item-list'}),
        error_messages={
            'invalid_choice': 'Invalid category'
        }
    )
    customer = forms.ModelChoiceField(
        label='Customer Name',
        queryset=Customer.objects.filter(is_deleted=False),
        empty_label='Select Customer',
        widget=forms.Select(attrs={'class': 'form-control customer-list'}),
        error_messages={
            'invalid_choice': 'Invalid category'
        }
    )

    quantity = forms.CharField(
        label='Quantity',
        widget=forms.TextInput(attrs={'class': 'form-control item-quantity', 'placeholder': '2'}),
    )

    total_price = forms.CharField(
        label='Total',
        widget=forms.TextInput(attrs={'class': 'form-control total-cost', 'disabled': True}),
        required=False,
    )

    class Meta:
        model = Transaction
        fields = {'item', 'quantity', 'customer', 'total_price'}


class CustomerForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shital Luitel'}),
        required=False,
    )

    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Biratnagar-04'}),
        required=False,
    )

    phone_number = forms.CharField(
        label='Phone no.',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '9842574872'}),
        required=False,
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

    def clean(self):
        cleaned_data = super(CustomerForm, self).clean()
        name = cleaned_data.get('name')
        phone_number = cleaned_data.get('phone_number')
        if Customer.objects.filter(name=name, phone_number=phone_number).exists():
            raise ValidationError("Customer with this Name and Phone number already exists.")
