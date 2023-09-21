from django import forms
from .models import Tweet, User, Profile

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm
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

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email',}))

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "New password"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Confirm new password"}))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'bio', 'profile_picture', 'cover_picture']
        widgets = {
            'display_name': forms.TextInput(attrs={'placeholder': 'Display Name'}),
            'bio': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tell us about yourself'}),
            'cover_picture': forms.FileInput(attrs={'style': 'display: none;'}),
            'profile_picture': forms.FileInput(attrs={'style': 'display: none;'}),
        }

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }
