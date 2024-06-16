from django import forms
from django.forms import ModelForm
from .models import Supplier,Customer
class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25,widget=forms.PasswordInput)

class RegisterCustomer(ModelForm,LoginForm):
    class Meta:
        model = Customer
        # fields = '__all__'
        exclude = ['user']
    field_order=['username','password','__all__']
        


class RegisterSupplier(ModelForm,LoginForm):
    class Meta:
        model = Supplier
        # fields = '__all__'
        exclude = ['user']
    field_order=['username','password','__all__']