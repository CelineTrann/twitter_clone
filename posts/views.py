from django.shortcuts import render, redirect
from .models import Tweet, User
from .forms import TweetForm

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    items = Tweet.objects.all().order_by("-updated_at")
    form = TweetForm()
    return render(request, "home.html", {"Tweets": items, "form": form})

def post(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("home")
        