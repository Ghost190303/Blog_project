from django import forms
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog
        fields=['Text', 'Image']

class UserRegistration(UserCreationForm):
    email = forms.EmailField()
    class meta:
        model = User
        fields= ('username','email','password1','password2')
