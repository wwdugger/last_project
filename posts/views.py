from re import template
from django.views.generic import PostListView, DetailView
from django.views.generic.edit import CreateView


class PostListView(ListView):
    template_name = "posts/list.html"
    model = "Post"


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = "Post"


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = "Post"
    fields = ["title", "subtitle", "body"]
