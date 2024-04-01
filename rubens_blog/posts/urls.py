from django.urls import path
from .views import PostListView, PostDetailView, PostUpdateView, PostCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("add/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/update/", PostUpdateView.as_view(template_name="posts/post_update.html"), name="post_update"),
]
