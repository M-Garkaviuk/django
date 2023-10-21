# users.views
from django.contrib.auth import logout
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from demo.models import Article, Comment


def user_profile_view(request, username="martinezmichelle"):
    user = get_object_or_404(User, username=username)
    articles = Article.objects.filter(author=user)
    return render(request, 'userprofile.html', {"user": user, "articles": articles})


def set_user_password_view(request):
    return HttpResponse("this page is to set user password")


def set_user_data_view(request):
    return HttpResponse("this page is to edit user's data")


def deactivate_user_view(request):
    return HttpResponse("This page deactivates user")


def register_user_view(request):
    return HttpResponse("This page to register a user")


def login_user_view(request):
    return render(request, "login.html", {"page_name": "Login page"})


def logout_user_view(request: HttpRequest) -> redirect:
    logout(request)
    return redirect('homepage')


def user_registration_view(request):
    return render(request, "registration.html", {"page_name": "Registration"})
