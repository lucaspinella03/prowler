from django import forms 
from .models import entry 

class entryForm(forms.ModelForm):
    class Meta:
        model = entry 
        fields = ['name','text']
        labels = {'name':'name','text':''}