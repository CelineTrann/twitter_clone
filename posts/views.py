from django.shortcuts import render, redirect
from .models import Tweet, Profile
from .forms import TweetForm

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

@login_required
def home(request):
    items = Tweet.objects.all().order_by("-updated_at")
    modal_form = TweetForm(prefix="modal")
    direct_form = TweetForm(prefix="direct")
    return render(request, "home.html", {"Tweets": items, "modal_form": modal_form, "direct_form": direct_form})

@login_required
def post(request):
    if request.method == 'POST':
        prev_link = request.META.get('HTTP_REFERER', '/')
        
        direct_form = TweetForm(request.POST, prefix='direct')
        if direct_form.is_valid():
            direct_tweet = direct_form.save(commit=False)
            direct_tweet.user = request.user
            direct_tweet.save()
            return redirect(home)

        modal_form = TweetForm(request.POST, prefix='modal')
        if modal_form.is_valid():
            modal_tweet = modal_form.save(commit=False)
            modal_tweet.user = request.user
            modal_tweet.save()
            return redirect(prev_link)
        
        return redirect(prev_link)

                
@login_required
def profile(request, username):
    modal_form = TweetForm(prefix="modal")
    profile_info = Profile.objects.get(pk=request.user.id)
    return render(request, "profile.html", {"modal_form": modal_form, "profile": profile_info})
    
        