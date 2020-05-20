from django import forms

class AddSitesForm(forms.Form):
    name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Give site a Name'}))
    location = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location Name '}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'You can add any detailed information'}))
    date = forms.DateField(widget=forms.DateInput())