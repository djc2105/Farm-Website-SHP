from django import forms
from website.models import Plant
import datetime

class PlantForm(forms.ModelForm):
    dateplanted = forms.DateField(label="Date Planted", widget=forms.TextInput(attrs={'type': 'date'}))
    plantname = forms.CharField(max_length=128, label="Plant Name")
    quantity = forms.IntegerField(label="Quantity Planted", min_value=0)

    class Meta:
        model = Plant
        exclude = ('row',)
