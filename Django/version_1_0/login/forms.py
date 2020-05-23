from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.shortcuts import render
from .models import Login

class LoginForm(forms.Form):
   username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
   
   def clean_message(self):
      username = self.cleaned_data.get("username")
      dbuser = Login.objects.filter(name = username)
      
      if not dbuser:
         raise forms.ValidationError("User does not exist in our db!")
      return username