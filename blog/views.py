# blog/views.py
from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.http import request

from .models import Post 

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin # new
)


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'BlogPostsList'

class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'DetailedPostObject'

class BlogCreateView(LoginRequiredMixin, CreateView): # new 
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']
    login_url = '/login/auth0'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,  UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    login_url = '/login/auth0'

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView): # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    login_url = '/login/auth0'

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

