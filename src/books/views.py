from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView, UpdateView, CreateView
from books.models import Autors, Genres, Publishers

def home_page(request):
    context = {}
    return render(request, template_name='home.html', context=context)

class AutorDetail(DetailView):
    model = Autors

class AutorDelete(DeleteView):
    model = Autors
    success_url = reverse_lazy('autors-list')

class AutorList(ListView):
    model = Autors

class AutorCreate(CreateView):
    model = Autors
    fields = ('first_name', 'last_name', 'date_of_birth', 'address')
    success_url = reverse_lazy('autors-list')

class AutorUpdate(UpdateView):
    model = Autors
    fields = ('first_name', 'last_name', 'date_of_birth')
    success_url = reverse_lazy('autors-list')

class GenreDetail(DetailView):
    model = Genres

class GenreDelete(DeleteView):
    model = Genres
    success_url = reverse_lazy('genres-list')

class GenreList(ListView):
    model = Genres

class GenreCreate(CreateView):
    model = Genres
    fields = ('name', )
    success_url = reverse_lazy('genres-list')

class GenreUpdate(UpdateView):
    model = Genres
    fields = ('name',)
    success_url = reverse_lazy('genres-list')

class PublisherDetail(DetailView):
    model = Publishers

class PublisherDelete(DeleteView):
    model = Publishers
    success_url = reverse_lazy('publishers-list')

class PublisherList(ListView):
    model = Publishers

class PublisherCreate(CreateView):
    model = Publishers
    fields = ('name', 'address')
    success_url = reverse_lazy('publishers-list')

class PublisherUpdate(UpdateView):
    model = Publishers
    fields = ('name', )
    success_url = reverse_lazy('publishers-list')