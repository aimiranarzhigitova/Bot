
from django.contrib import admin
from .models import *
from .forms import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'extenal_id', 'name')
    form = ProfileForm


@admin.register(Message)
class Message(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at')