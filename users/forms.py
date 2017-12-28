from  django import forms
from django.contrib.auth.models import User

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','password']

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=50)
    password = forms.CharField(label='Password',max_length=50,widget=forms.PasswordInput)