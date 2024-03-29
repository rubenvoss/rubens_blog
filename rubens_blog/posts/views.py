from django.shortcuts import render
from .models import Post
import markdown

def post_view(request):
    post = Post.objects.first()
    md = markdown.Markdown(extensions=["fenced_code"])
    post.content = md.convert(post.content)
    context = {"post": post}
    return render(
        request,
        "posts/post.html",
        context=context
    )