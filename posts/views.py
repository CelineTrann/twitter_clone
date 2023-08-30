from django.shortcuts import render
from .models import Tweet, User

from django.http import HttpResponse

# Create your views here.
def home(request):
    items = Tweet.objects.all().order_by("-updated_at")
    return render(request, "home.html", {"Tweets": items})

def post(request):
    if request.method == 'POST':
        content = request.POST['text-area']
        return HttpResponse(content)