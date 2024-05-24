from django.urls import path
from .views import PostListView, PostDetailView, PostUpdateView, PostCreateView, convert_markdown

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("add/", PostCreateView.as_view(), name="post_create"),
    path("<slug:slug>", PostDetailView.as_view(), name="post_detail"),
    path("<slug:slug>/update/", PostUpdateView.as_view(), name="post_update"),
]

htmx_urlpatterns = [
    path("convert_markdown/", convert_markdown, name="convert_markdown")
]

urlpatterns += htmx_urlpatterns