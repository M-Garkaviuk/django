
from demo.models import Article, Comment
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def article_list(request):
    articles = Article.objects.filter(created__lte=timezone.now()).order_by('created')
    return render(request, 'main_page.html', {"articles": articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=article)
    return render(request, "article_detail.html", {"article": article, "comments": comments})