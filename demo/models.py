from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Topic(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(User, through="Notification")

    def __str__(self):
        return f'ID: {self.pk}, {self.title}'


class Notification(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriber")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    is_notified = models.BooleanField(default=False)


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="articles")
    topics = models.ManyToManyField(Topic, related_name="topics")

    def __str__(self):
        return f"ID = {self.pk}, subject - {self.title}"


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, related_name="article")

    def __str__(self):
        return self.message

    # def get_absolute_url(self):
    #     return reverse('main:article_detail',
    #                    args=[str(self.pk)])
