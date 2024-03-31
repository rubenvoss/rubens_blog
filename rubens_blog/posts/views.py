from .models import Post
from django.views import generic

class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post