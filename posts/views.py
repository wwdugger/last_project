from django.shortcuts import render, redirect, get_object_or_404
from re import template
from multiprocessing import context
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post, Status
from .models import Post

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class DraftPostListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name='draft')
        context['post_list'] = Post.objects.filter(
                                        status=pending_status
                                        ).order_by(
                                            'created_on').reverse()
        return context

class PublishedPostListView(ListView):
    template_name = "post/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="published")
        context["post_list"] = Post.objects.filter(
                                    author=self.request.user
                                    ).filter(
                                        status=pending_status).order_by(
                                            'created_on').reverse()
        return context


class ArchivedPostListView(ListView):
    template_name = "post/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        archived_status = Status.objects.get(name="archived")
        context["post_list"] = Post.objects.filter(
                                    author=self.request.user
                                    ).filter(
                                        status=archived_status
                                        ).order_by('title')
                                                
        return context

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle","status","body"]

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        post_obj = self.getobject()
        return post_obj == self.request.user

    def PostDetail(request, post_id):
        post = get_object_or_404(Post, id=post_id)

        #comment
        comments = Comment.objects.filter(post=post).order_by

        #comment_form



        
        context = {
            'post': post
        }
        return render(request, 'post-dtails', context)