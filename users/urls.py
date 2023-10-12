# users.urls
from django.urls import path, re_path
from users.views import (user_profile_view,
                        set_user_password_view,
                        set_user_data_view,
                        login_user_view,
                        logout_user_view,
                         user_registration_view,)


urlpatterns = [
    path("profile/<str:username>/", user_profile_view, name="user_profile"),
    path("set-password/", set_user_password_view, name="set_user_password"),
    path("set-userdata/", set_user_data_view, name="set_user_password"),
    path("login/", login_user_view, name='login'),
    path("logout/", logout_user_view, name='logout'),
    path("registration/",  user_registration_view, name='registration')
    ]
