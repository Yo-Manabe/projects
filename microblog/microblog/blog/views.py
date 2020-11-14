from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse_lazy
from django.contrib import messages

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Blog

from .forms import BlogForm


class BlogListView (ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView (DetailView):
    model = Blog
    
class BlogCreateView (LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    #fields = ["content"]
    success_url = reverse_lazy("index")
    login_url = '/login'
    template_name = "blog/blog_create_form.html"
    
    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, "保存に失敗しました")
        return super().form_invalid(form)
    
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    #fields = ["content",]
    login_url = '/login'
    template_name = "blog/blog_update_form.html"
    
    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs ={"pk": blog_pk})
        return url
        
    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_valid(form)

class BlogDeleteView (LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("index")
    login_url = '/login'
    