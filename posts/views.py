from django.shortcuts import render, HttpResponse
from .models import Tweet

# Create your views here.
def home(request):
    items = Tweet.objects.all()
    return render(request, "home.html", {"Tweets": items})