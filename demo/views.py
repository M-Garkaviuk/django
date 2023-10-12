# demo.views
from django.http import HttpResponse
from django.shortcuts import render


def homepage_view(request):
    return render(request, "index.html")


def about_view(request):
    return render(request, "about.html")


def main_article_view(request, article: int):
    return HttpResponse(f"article # {article}")


def comments_article_view(request, article: int):
    return HttpResponse(f'This is a page for comments for article # {article}')


def create_article_view(request):
    return render(request, "newarticle.html")


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



