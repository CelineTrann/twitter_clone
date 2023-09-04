from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Tweet, Profile

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "password", "date_joined"]
    inlines = [ProfileInline]

    def get_inlines(self, request, obj=None):
        if obj:
            return [ProfileInline]
        else:
            return []

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(Tweet)