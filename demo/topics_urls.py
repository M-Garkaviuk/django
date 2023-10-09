from django.urls import path
from demo import views


urlpatterns = [
    path("topics/", views.topics_list_view, name="topics"),
    path("topics/<str:topic>/subscribe/", views.topic_subscribe_view, name="topic_subscribe"),
    path("topics/<str:topic>/unsubscribe/", views.topic_unsubscribe_view, name="topic_unsubscribe"),
]
