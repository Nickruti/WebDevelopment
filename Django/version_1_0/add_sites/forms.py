from django import forms
from bootstrap_datepicker_plus import DatePickerInput

class AddSitesForm(forms.Form):
    name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Site Name'}))
    location = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location Name '}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Any Detailed Information about Site'}))
    date = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y', attrs={"placeholder": "Site Work Started On"}))