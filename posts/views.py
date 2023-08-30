from django.shortcuts import render, HttpResponse
from .models import Tweet, User

# Create your views here.
def home(request):
    items = Tweet.objects.all().order_by("-updated_at")
    return render(request, "home.html", {"Tweets": items})