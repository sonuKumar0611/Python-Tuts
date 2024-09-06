from django import forms
from .models import Customer

# Create the FormName class
class FormName(forms.Form):
    first_name = forms.CharField() 
    last_name = forms.CharField() 
    phone = forms.CharField() 
    email = forms.EmailField() 
    password = forms.CharField() 

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone','email','password']

