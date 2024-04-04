from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from .models import Post

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
    return HttpResponse("hello world")