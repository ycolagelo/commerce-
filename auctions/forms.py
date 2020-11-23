from django import forms
from .models import Listing, Choices, Bid


class NewListForm(forms.ModelForm):
    """classes for the created list"""
    price = forms.DecimalField(label="Price", required=True)
    description = forms.CharField(
        label="Description", required=True, max_length=500)
    category = forms.CharField(
        label="Category",
        required=True,
        widget=forms.Select(choices=Choices.choices))
    name = forms.CharField(label="name", required=True)
    image = forms.ImageField(label="image", required=False)

    class Meta:
        model = Listing
        fields = ("price", "description", "category", "name", "image")


class NewBid(forms.ModelForm):
    """verification of the bid form"""
    bid = forms.DecimalField(label="bid", required=True)

    class Meta:
        model = Bid
        fields = ("bid",)
