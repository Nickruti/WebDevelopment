from django import forms
from .models import Materials
from bootstrap_datepicker_plus import DatePickerInput

class DailyUpdateForm(forms.Form):
    date = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y', attrs={"placeholder": "Date for Updated work"}))
    total_workers = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total workers assigned today'}))
    male_coolie = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Male Coolies in total'}))
    female_coolie = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Female Coolies in total'}))
    mason = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Masons in total'}))
    centrinc_fitter = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Centric Fitters in total'}))
    materials_purchased = forms.ModelChoiceField(queryset=Materials.objects.all(), empty_label='Select Materials Purchased')
    material_details = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Amount Spend/Purchasedd or any other details'}))