from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm, CustomPasswordResetForm, CustomSetPasswordForm

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
    path("accounts/registration", views.registration, name="registration"),
    path("accounts/profile_creation", views.profile_creation, name="profile_creation"),
    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm), name='password_reset'),
    path("accounts/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(form_class=CustomSetPasswordForm), name='password_reset_confirm'),

    path("settings/profile", views.edit_profile, name="edit_profile"),
    path("settings/account", views.settings, name="settings"),
    path("settings/account/change_password", views.change_password, name="change_password"),
]