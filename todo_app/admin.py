from django.contrib import admin
from .models import Task, Post, Event
# Register your models here.

admin.site.register(Task)
admin.site.register(Post)
admin.site.register(Event)
