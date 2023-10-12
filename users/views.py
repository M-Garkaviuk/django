# users.views
from django.contrib.auth import logout
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render


def user_profile_view(request, username: str):
    return HttpResponse(f'This is profile page of {username}')


def set_user_password_view(request):
    return HttpResponse("this page is to set user password")


def set_user_data_view(request):
    return HttpResponse("this page is to edit user's data")


def deactivate_user_view(request):
    return HttpResponse("This page deactivates user")


def register_user_view(request):
    return HttpResponse("This page to register a user")


def login_user_view(request):
    return render(request, "login.html")


def logout_user_view(request: HttpRequest) -> redirect:
    logout(request)
    return redirect('homepage')


def user_registration_view(request):
    return render(request, "registration.html")
