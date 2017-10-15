from django import forms
from items.models import Item
from .models import Transaction
from customers.models import Customer


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
        widget=forms.TextInput(attrs={'class': 'form-control total-cost','disabled': True}),
        required=False,
    )

    class Meta:
        model = Transaction
        fields = {'item', 'quantity', 'customer', 'total_price'}
