from django import forms
from .models import Image, Choices


class NewListForm(forms.Form):
    """classes for the created list"""
    price = forms.DecimalField(label="Price", required=True)
    description = forms.CharField(
        label="Description", required=True, max_length=500)
    category = forms.CharField(
        label="Category",
        required=True,
        widget=forms.Select(choices=Choices.choices))


class ImageForm(forms.ModelForm):
    """form for image"""
    class Meta:
        model = Image
        fields = ["name", "image"]
