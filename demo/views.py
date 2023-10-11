# demo.views
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage_view(request):
    return HttpResponse("homepage")


def about_view(request):
    return HttpResponse("about")


def main_article_view(request, article: int):
    return HttpResponse(f"article # {article}")


def comments_article_view(request, article: int):
    return HttpResponse(f'This is a page for comments for article # {article}')


def create_article_view(request):
    return HttpResponse(f'This is a page for article creation')


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


def bla(request):
    return render(request, template_name="bla.html")


def bla2(request):
    return render(request, template_name="bla2.html")

