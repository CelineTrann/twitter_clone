from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm

urlpatterns = [
    path("", views.home, name="home"),
    path("post/", views.post, name="post"),
    path("reply/<int:tweet_id>", views.reply, name="reply"),
    path("delete/<int:tweet_id>", views.delete_tweet, name="delete_tweet"),
    path("like/<int:tweet_id>", views.like_tweet, name="like_tweet"),
    path("retweet/<int:tweet_id>", views.retweet_tweet, name="retweet_tweet"),

    path("profile/<str:request_username>", views.profile, name="profile"),
    path("profile/<str:request_username>/likes", views.profile_likes, name="profile_likes"),
    path("profile/<str:request_username>/status/<int:tweet_id>", views.tweet_detail, name="tweet_detail"),
    
    path("profile/<str:request_username>/following", views.follow, name="following"),
    path("profile/<str:request_username>/followers", views.follow, name="followers"),
    path("follow/", views.follow_unfollow, name="follow_unfollow"),

    path("accounts/login/", auth_views.LoginView.as_view(authentication_form=CustomLoginForm), name='login'),
    path("account/registration", views.registration, name="registration"),
    path("account/profile_creation", views.profile_creation, name="profile_creation"),
]
