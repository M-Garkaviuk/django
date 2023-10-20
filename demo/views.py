# demo.views
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.utils import timezone
from demo.models import Article


def homepage_view(request):
    return render(request, "main_page.html", {"article": "articles"})


def about_view(request):
    return render(request, "about.html", {"page_name": "About"})


def main_article_view(request, article: int):
    return HttpResponse(f"article # {article}")


def comments_article_view(request, article: int):
    return HttpResponse(f'This is a page for comments for article # {article}')


def create_article_view(request):
    return render(request, "newarticle.html", {"page_name": "New Article"})


def update_article_view(request,  article: int):
    return HttpResponse(f'This is a page to update article # {article}')


def delete_article_view(request, article: int):
    return HttpResponse(f'This page to confirm removal of article #{article}')


def topics_list_view(request):
    return HttpResponse(f'This page lists all the topics available on this blog')


def topic_subscribe_view(request, topic: str):
    return HttpResponse(f'This page is to confirm subscription on the topic {topic}')


def topic_unsubscribe_view(request, topic: str):
    return HttpResponse(f'This page is to confirm unsubscription from the topic {topic}')


def article_list(request):
    articles = Article.objects.filter(created__lte=timezone.now()).order_by('created')
    return render(request, 'main_page.html', {"articles": articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "article_detail.html", {"article": article})




