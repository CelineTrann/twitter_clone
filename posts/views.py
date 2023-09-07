from django.shortcuts import render, redirect
from .models import Tweet, Profile, User
from .forms import TweetForm, UserProfileForm, CustomUserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from django.http import HttpResponse

def registration(request):
    if request.method == 'GET':
        user_form = CustomUserCreationForm()
        return render(request, "registration/registration.html", {"user_form": user_form})
    
    elif request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect(profile_creation)
        else:
            return render(request, "registration/registration.html", {"user_form": user_form})
        
@login_required
def profile_creation(request):
    if request.method == 'GET':
        profile_form = UserProfileForm(instance=request.user)
        return render(request, "registration/profile-creation.html", {"profile_form": profile_form})
    
    elif request.method == 'POST':
        Profile.objects.create(user=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.profile)
        profile_form.save()
        return redirect(home)

@login_required
def home(request):
    if not hasattr(request.user, 'profile'):
        return redirect(profile_creation)
    
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
def profile(request, request_username):
    if not hasattr(request.user, 'profile'):
        return redirect(profile_creation)
    
    modal_form = TweetForm(prefix="modal")
    profile_info = Profile.objects.get(user__username = request_username)
    items = Tweet.objects.filter(user__username = request_username).order_by("-updated_at")
    return render(request, "profile.html", {"modal_form": modal_form, "profile": profile_info, 'Tweets': items})
    
@login_required
def follow(request, request_username):
    curr_profile = Profile.objects.get(user__username = request_username)
    if request.path == f"/profile/{request_username}/following":
        following_list = curr_profile.follows.exclude(follows = curr_profile)
        return render(request, "follow.html", {"profile": curr_profile, "follow_list": following_list, "type": "following"})
    else: 
        follower_list = curr_profile.followed_by.exclude(followed_by = curr_profile)
        return render(request, "follow.html", {"profile": curr_profile, "follow_list": follower_list, "type": "followers"})
        

def follow_unfollow(request):
    if request.method == 'POST':
        current_user_profile = Profile.objects.get(user__username = request.user.username)
        follow_profile_id = request.POST.get("follow")
        follow_profile = Profile.objects.get(pk=follow_profile_id)
        
        if follow_profile not in current_user_profile.follows.all():
            current_user_profile.follows.add(follow_profile_id)
        else:
            current_user_profile.follows.remove(follow_profile_id)

        current_user_profile.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))
