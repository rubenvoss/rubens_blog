from django.shortcuts import render
from .models import Post
from django.views import generic

def post_view(request):
    post = Post.objects.first()
    context = {"post": post}
    return render(
        request,
        "posts/post.html",
        context=context
    )

class PostListView(generic.ListView):
    model = Post