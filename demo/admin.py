
from django.contrib import admin
from .models import Topic, Article, Comment, Notification

admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Notification)
