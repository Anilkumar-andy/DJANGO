from django import forms

gender_choice=[
    ('m','Male'),
    ('f','Femlae')]

class RegisterForm(forms.Form):
    Firstname = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    Gender = forms.ChoiceField(choices=gender_choice)
    Password = forms.CharField(max_length=30, widget=forms.PasswordInput)