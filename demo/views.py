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

class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True
    })
