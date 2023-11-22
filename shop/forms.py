from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

# class CustomUserForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The Username'}))
#     email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The email'}))
#     password1 = forms.PasswordInput(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The password'}))
#     password2 = forms.PasswordInput(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The confirm password2'}))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class CustomUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The Username'}))
        self.fields['email'] = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The email'}))
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter the password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm the password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']