from django.contrib import admin
from .models import Tweet, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tweet)