from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.urls import reverse_lazy
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
   
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post-details.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogEditView(UpdateView):
    model = Post
    template_name = 'post-edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')

