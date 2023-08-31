from django.shortcuts import render, redirect
from .models import Tweet, User
from .forms import TweetForm

from django.http import HttpResponse

# Create your views here.
def home(request):
    items = Tweet.objects.all().order_by("-updated_at")
    form = TweetForm()
    return render(request, "home.html", {"Tweets": items, "form": form})

def post(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        