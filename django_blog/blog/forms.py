from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class signupform(UserCreationForm):
    email = forms.EmailField(max_length=254,help_text='Required.inform  valid email address.')
class Meta:
    model = User 
    fields =['username','email','password2']
class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']