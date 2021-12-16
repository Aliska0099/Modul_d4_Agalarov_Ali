from datetime import datetime
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Author, Category, Post, Comment
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView

from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .filters import NewsFilter
from .forms import NewsForm


class NewsList(ListView):
    model = Post
    template_name = 'newsPort_list.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsSearch(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']
    paginate_by = 5


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context





class NewsDetailView(DetailView):
    template_name = 'newsPort_detail.html'
    queryset = Post.objects.all()



class NewsAddView(CreateView):
    template_name = 'news_add.html'
    form_class = NewsForm
    success_url = '/news/'



class NewsEditView(UpdateView):
    template_name = 'newsP_edit.html'
    form_class = NewsForm
    success_url = '/news/'


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)



class NewsDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'