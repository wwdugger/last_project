from re import template
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
