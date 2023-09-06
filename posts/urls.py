from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm

urlpatterns = [
    path("", views.home, name="home"),
    path("post/", views.post, name="post"),
    path("profile/<str:request_username>", views.profile, name="profile"),
    path("profile/<str:request_username>/following", views.follow, name="following"),
    path("profile/<str:request_username>/followers", views.follow, name="followers"),

    path("accounts/login/", auth_views.LoginView.as_view(authentication_form=CustomLoginForm), name='login'),
    path("account/registration", views.registration, name="registration"),
    path("account/profile_creation", views.profile_creation, name="profile_creation"),
]
