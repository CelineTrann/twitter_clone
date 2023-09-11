from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=60)
    bio = models.TextField(max_length=255, blank=True)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    content = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, through="Tweet_Likes", related_name='tweet_like')
    retweets = models.ManyToManyField(User, through="Tweet_Retweets", related_name='retweeted_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    
class Tweet_Likes(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.DO_NOTHING)
    curr_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

class Tweet_Retweets(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.DO_NOTHING)
    curr_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)