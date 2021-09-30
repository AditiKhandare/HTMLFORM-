from django.core import validators
from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'address', 'email', 'mobile_no']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'mobile_no': forms.TextInput(attrs={'class':'form-control'}),
            #'image': forms.FileInput(attrs={'class':'form-control'}),
            
        }