from django import forms
from .categories import CATEGORIES

class CreateListingForm(forms.Form):
    title = forms.CharField(label='Item name', max_length=64)
    description = forms.CharField(label='Item description', max_length=500, widget=forms.Textarea)
    price = forms.DecimalField(label='Starting price', max_digits=10, decimal_places=2)
    image = forms.URLField(required=False)
    category = forms.ChoiceField(choices=CATEGORIES, label='Category', initial='Select', required=False)