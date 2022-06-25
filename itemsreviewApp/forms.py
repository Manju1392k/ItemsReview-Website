
from django.forms import ModelForm
from django import forms

from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['Author_Name','Product_Name', 'Product_Review', 'Product_Image']

    Author_Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Product_Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Product_Review = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    Product_Image = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))