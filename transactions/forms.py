from django import forms
from items.models import Item
from .models import Transaction


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

    quantity = forms.CharField(
        label='Quantity',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2'})
    )

    customer_name = forms.CharField(
        label='Customer Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hari Neupane'})
    )

    class Meta:
        model = Transaction
        fields = {'item', 'quantity', 'customer_name'}
