from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from .models import Post
from .templatetags.post_conversion import return_markdown
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/admin/login/"
    redirect_field_name = "next"
    model = Post
    fields = [ "title", "content" ]

class PostCreateView(CreateView):
    model = Post
    fields = [ "title", "content" ]

def convert_markdown(request):
    content = request.POST.get("content")
    content = return_markdown(content)
    return HttpResponse(content)