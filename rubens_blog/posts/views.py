from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from .models import Post
from .templatetags.post_conversion import return_markdown

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = [ "title", "content" ]

class PostCreateView(CreateView):
    model = Post
    fields = [ "title", "content" ]

def convert_markdown(request):
    content = request.POST.get("content")
    content = return_markdown(content)
    return HttpResponse(content)