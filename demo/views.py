# demo.views
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from demo.models import Article, Comment
from datetime import datetime
from django.utils import timezone


def about_view(request):
    return render(request, "about.html", {"page_name": "About"})


def main_article_view(request, article: int):
    return HttpResponse(f"article # {article}")


def create_article_view(request):
    return render(request, "newarticle.html", {"page_name": "New Article"})


def update_article_view(request,  article):
    article = get_object_or_404(Article, pk=article)
    return render(request,"updatearticle.html", {'article': article})


def delete_article_view(request, article):
    article = get_object_or_404(Article, pk=article)
    return render(request, "deletearticle.html", {'article': article})


def topics_list_view(request):
    return HttpResponse(f'This page lists all the topics available on this blog')


def topic_subscribe_view(request, topic: str):
    return HttpResponse(f'This page is to confirm subscription on the topic {topic}')


def topic_unsubscribe_view(request, topic: str):
    return HttpResponse(f'This page is to confirm unsubscription from the topic {topic}')






