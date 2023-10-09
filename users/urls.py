# users.urls
from django.urls import path, re_path
from users import views


urlpatterns = [
    path("profile/<str:username>/", views.user_profile_view, name="user_profile"),
    path("set-password/", views.set_user_password_view, name="set_user_password"),
    path("set-userdata/", views.set_user_data_view, name="set_user_password"),
    path("login/", views.login_user_view, name='login'),
    path("logout/", views.logout_user_view, name='logout'),
    ]
