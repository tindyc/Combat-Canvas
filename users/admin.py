from django.contrib import admin

# Register your models here.
from .models import Profile, Message

admin.site.register(Profile)
admin.site.register(Message)
