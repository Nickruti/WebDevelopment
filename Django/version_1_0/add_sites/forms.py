from django import forms

class AddSitesForm(forms.Form):
    name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Site Name'}))
    location = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location Name '}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Any Detailed Information about Site'}))
    date = forms.DateField(widget=forms.DateInput(attrs={"placeholder": "Site Work Started On"}))