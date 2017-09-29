from django import forms
from units.models import Unit
from .models import Item


class ItemForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'दाल'}),
    )

    unit_price = forms.DecimalField(
        label='Unit Price',
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': '6'})
    )

    # this is used to create select box
    unit = forms.ModelChoiceField(
        label='Unit',
        queryset=Unit.objects.all(),
        empty_label='Select Unit',
        widget=forms.Select(attrs={'class': 'form-control'}),
        error_messages={
            'invalid_choice': 'Invalid category'
        }
    )

    class Meta:
        model = Item
        fields = {
            'name',
            'unit_price',
            'unit',
        }
