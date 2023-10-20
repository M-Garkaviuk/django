# demo.urls

from django.urls import path
from demo.views import (homepage_view,
                        about_view,
                        create_article_view,
                        article_list,
                        comments_article_view,
                        update_article_view,
                        topics_list_view,
                        topic_subscribe_view,
                        topic_unsubscribe_view,
                        article_detail,
                        )


urlpatterns = [
    path('', article_list, name='homepage'),
    path("about/", about_view, name="about"),
    path("create/", create_article_view, name="create_article"),
    path("article/<int:pk>/", article_detail, name="article_detail"),
    path("article/<int:article>/comments", comments_article_view, name="comments"),
    path("article/<int:article>/update", update_article_view, name='update_article'),
    path("topics/", topics_list_view, name="topics"),
    path("topics/<str:topic>/subscribe/", topic_subscribe_view, name="topic_subscribe"),
    path("topics/<str:topic>/unsubscribe/", topic_unsubscribe_view, name="topic_unsubscribe"),
]
