# demo.urls

from django.urls import path
from demo.views import (about_view,
                        create_article_view,
                        update_article_view,
                        topics_list_view,
                        topic_subscribe_view,
                        topic_unsubscribe_view,
                        delete_article_view

                        )
from demo.services import article_list, article_detail


urlpatterns = [
    path('', article_list, name='homepage'),
    path("about/", about_view, name="about"),
    path("create/", create_article_view, name="create_article"),
    path("article/<int:pk>/", article_detail, name="article_detail"),
    path("article/<int:article>/update", update_article_view, name='update_article'),
    path("article/<int:article>/delete", delete_article_view, name='delete_article'),
    path("topics/", topics_list_view, name="topics"),
    path("topics/<str:topic>/subscribe/", topic_subscribe_view, name="topic_subscribe"),
    path("topics/<str:topic>/unsubscribe/", topic_unsubscribe_view, name="topic_unsubscribe"),

]
