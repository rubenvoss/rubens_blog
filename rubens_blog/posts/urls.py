from django.urls import path
from .views import post_view, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("post/", post_view, name="post"),
]
