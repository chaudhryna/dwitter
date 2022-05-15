from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Dweet

class ProfileInline(admin.StackedInline):
    model = Profile

admin.site.register(Dweet)

