# demo.urls

from django.urls import path
from demo import views


urlpatterns = [
    path("", views.homepage_view, name="homepage"),
    path("about/", views.about_view, name="about"),
    path("create/", views.create_article_view, name="create_article"),
]

