from django.shortcuts import render, redirect
from .models import Tweet, Profile
from .forms import TweetForm

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

@login_required
def home(request):
    items = Tweet.objects.all().order_by("-updated_at")
    form = TweetForm()
    return render(request, "home.html", {"Tweets": items, "form": form, "User": request.user})

@login_required
def post(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("home")
        
@login_required
def profile(request, username):
    profile_info = Profile.objects.get(pk=request.user.id)
    return render(request, "profile.html", {"Profile": profile_info})
    
        