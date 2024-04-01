from django.urls import path
from .views import PostListView, PostDetailView, PostEditView

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("<int:pk>/edit/", PostEditView.as_view(template_name="posts/post_edit.html"), name="post-edit"),
]
