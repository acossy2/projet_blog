from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['titre', 'contenu', 'auteur', 'image']

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['titre', 'contenu', 'auteur', 'image']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')
