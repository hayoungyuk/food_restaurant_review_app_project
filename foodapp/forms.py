from django import forms
from .models import Foodapp

class FoodappForm(forms.ModelForm):
    class Meta:
        model = Foodapp
        fields = ['location','eater','content','photos']