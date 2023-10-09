from django.urls import path
from demo import views

urlpatterns = [
    path("<int:article>/", views.main_article_view, name="article"),
    path("<int:article>/comments", views.comments_article_view, name="comments"),
    path("<int:article>/update", views.update_article_view, name='update_article'),

]

