# demo.urls

from django.urls import path
from demo.views import (homepage_view,
                        about_view,
                        create_article_view,
                        main_article_view,
                        comments_article_view,
                        update_article_view,
                        topics_list_view,
                        topic_subscribe_view,
                        topic_unsubscribe_view,
                        )


urlpatterns = [
    path("", homepage_view, name="homepage"),
    path("about/", about_view, name="about"),
    path("create/", create_article_view, name="create_article"),
    path("<int:article>/", main_article_view, name="article"),
    path("<int:article>/comments", comments_article_view, name="comments"),
    path("<int:article>/update", update_article_view, name='update_article'),
    path("topics/", topics_list_view, name="topics"),
    path("topics/<str:topic>/subscribe/", topic_subscribe_view, name="topic_subscribe"),
    path("topics/<str:topic>/unsubscribe/", topic_unsubscribe_view, name="topic_unsubscribe"),
]

