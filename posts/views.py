from django.shortcuts import render, redirect
from .models import Tweet, Profile, User, Tweet_Retweets, Tweet_Convo
from .forms import TweetForm, UserProfileForm, CustomUserCreationForm

from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q

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
    
    tweets = list(Tweet.objects \
                .filter(Q(user__profile__followed_by=request.user.profile) | Q(user=request.user)) \
                .order_by("-updated_at") \
                .distinct())
    retweet_dates = list(Tweet_Retweets.objects. \
                filter(curr_user__profile__in=request.user.profile.follows.all()) \
                .order_by("-created_at"))
    items = tweet_join_retweet(tweets, retweet_dates)

    modal_form = TweetForm(prefix="modal")
    direct_form = TweetForm(prefix="direct")
    return render(request, "home.html", {"Tweets": items, "modal_form": modal_form, "direct_form": direct_form})

@login_required
def post(request):
    prev_link = request.META.get('HTTP_REFERER', '/')

    if request.method == 'POST':        
        direct_form = TweetForm(request.POST, prefix='direct')
        if direct_form.is_valid():
            direct_tweet = direct_form.save(commit=False)
            direct_tweet.user = request.user
            direct_tweet.save()
            direct_new_convo = Tweet_Convo.objects.create(tweet=direct_tweet)
            direct_new_convo.save()
            return redirect(home)

        modal_form = TweetForm(request.POST, prefix='modal')
        if modal_form.is_valid():
            modal_tweet = modal_form.save(commit=False)
            modal_tweet.user = request.user
            modal_tweet.save()
            modal_new_convo = Tweet_Convo.objects.create(tweet=modal_tweet)
            modal_new_convo.save()
            return redirect(prev_link)
        
    return redirect(prev_link)

@login_required
def delete_tweet(request, tweet_id):
    try:
        Tweet.objects.get(id=tweet_id, user=request.user).delete()
    except Tweet.DoesNotExist:
        raise PermissionDenied("User can't delete this tweet.")
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def like_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    if tweet.likes.filter(id=request.user.id).exists():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def retweet_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    if tweet.retweets.filter(id=request.user.id).exists():
        tweet.retweets.remove(request.user)
    else: 
        tweet.retweets.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', '/'))
                
@login_required
def profile(request, request_username):
    if not hasattr(request.user, 'profile'):
        return redirect(profile_creation)
    
    modal_form = TweetForm(prefix="modal")
    profile_info = Profile.objects.get(user__username = request_username)

    tweets = list(Tweet.objects.filter(user__username=request_username).order_by("-updated_at"))
    retweet_dates = list(Tweet_Retweets.objects.filter(curr_user__username=request_username).order_by("-created_at"))
    items = tweet_join_retweet(tweets, retweet_dates)

    return render(request, "profile.html", {"modal_form": modal_form, "profile": profile_info, 'Tweets': items, "type": 'posts'})

@login_required
def profile_likes(request, request_username):
    if not hasattr(request.user, 'profile'):
        return redirect(profile_creation)

    modal_form = TweetForm(prefix="modal")
    profile_info = Profile.objects.get(user__username = request_username)
    items = Tweet.objects.filter(likes__username=request_username).order_by("-tweet_likes__created_at")
    return render(request, "profile.html", {"modal_form": modal_form, "profile": profile_info, 'Tweets': items, "type": 'likes'})
    
    
@login_required
def follow(request, request_username):
    curr_profile = Profile.objects.get(user__username = request_username)
    if request.path == f"/profile/{request_username}/following":
        following_list = curr_profile.follows.exclude(follows = curr_profile)
        return render(request, "follow.html", {"profile": curr_profile, "follow_list": following_list, "type": "following"})
    else: 
        follower_list = curr_profile.followed_by.exclude(followed_by = curr_profile)
        return render(request, "follow.html", {"profile": curr_profile, "follow_list": follower_list, "type": "followers"})
        
@login_required
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

@login_required
def tweet_detail(request, request_username, tweet_id):
    curr_user = User.objects.get(username=request_username)
    modal_form = TweetForm(prefix="modal")

    original_tweet = Tweet.objects.get(id=tweet_id)
    reply_form = TweetForm(prefix="reply")

    current_convo = Tweet_Convo.objects.filter(reply_to__id=tweet_id)
    tweets = [x.tweet for x in current_convo]
    # parent = Tweet.objects.filter(convo_tweet=tweet_id)

    return render(request, "detail.html", {"original_tweet": original_tweet, "reply_form": reply_form, "Tweets": tweets, "modal_form": modal_form})

@login_required
def reply(request, tweet_id):
    prev_link = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        reply_form = TweetForm(request.POST, prefix='reply')
        if reply_form.is_valid():
            reply_tweet = reply_form.save(commit=False)
            reply_tweet.user = request.user
            reply_tweet.save()

            convo_id = Tweet_Convo.objects.get(tweet_id=tweet_id).conversation_id
            original_tweet = Tweet.objects.get(id=tweet_id)
            new_reply = Tweet_Convo.objects.create(conversation_id=convo_id, reply_to=original_tweet, tweet=reply_tweet)
            new_reply.save()

    return redirect(prev_link)


def tweet_join_retweet(tweets, retweets):
    items = []
    t, r = 0, 0
    while (t < len(tweets) and r < len(retweets)):
        curr_retweet, curr_tweet = retweets[r], tweets[t]
        if curr_retweet.created_at > curr_tweet.updated_at:
            curr_retweet.tweet.retweeted_by = curr_retweet.curr_user
            items.append(curr_retweet.tweet)
            r += 1
        else:
            items.append(curr_tweet)
            t += 1

    if t < len(tweets):
        items += tweets[t:]

    if r < len(retweets):
        items += retweets[r:].tweet

    return items