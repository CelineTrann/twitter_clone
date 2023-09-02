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
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
        
        return redirect(request.META.get('HTTP_REFERER', '/'))

                
@login_required
def profile(request, username):
    form = TweetForm(prefix='modal')
    profile_info = Profile.objects.get(pk=request.user.id)
    return render(request, "profile.html", {"form": form, "Profile": profile_info})
    
        