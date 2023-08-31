from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'tweet-content', 'rows': 7, 'placeholder': 'What\'s happening?'}),
        }