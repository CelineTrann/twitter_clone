from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm

urlpatterns = [
    path("", views.home, name="home"),
    path("post/", views.post, name="post"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("accounts/login/", auth_views.LoginView.as_view(authentication_form=CustomLoginForm), name='login'),
]
