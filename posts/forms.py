from django import forms
from .models import Tweet, User, Profile

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'tweet-content', 'rows': 3, 'placeholder': 'What\'s happening?'}),
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'bio']
        widgets = {
            'display_name': forms.TextInput(attrs={'placeholder': 'Display Name'}),
            'bio': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Tell us about yourself'}),
        }

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Confirm Password'}))

