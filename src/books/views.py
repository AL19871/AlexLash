from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView, UpdateView, CreateView
from books.models import Autors, Genres, Publishers, BooksList, Series

class BookList(ListView):
    model = BooksList

class BookDetail(DetailView):
    model = BooksList

class BookDelete(DeleteView):
    model = BooksList
    success_url = reverse_lazy('books-list')

class BookCreate(CreateView):
    model = BooksList
    fields = ('name', 'image', 'cost', 'author', 'seria', 'genre', 'year_of_publishing', 'number_of_pages', 'binding', 
        'format_of_book', 'ISBN', 'weight', 'age_restrictions', 'publisher', 'amount', 'active', 'rating')
    success_url = reverse_lazy('books-list')

class BookUpdate(UpdateView):
    model = BooksList
    fields = ('name', 'cost', 'amount', 'active')
    template_name = 'bookslist_update.html'
    success_url = reverse_lazy('books-list')

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
    template_name = 'autors_update.html'
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
    fields = ('name', 'descpiption')
    success_url = reverse_lazy('genres-list')

class GenreUpdate(UpdateView):
    model = Genres
    fields = ('name', 'descpiption')
    template_name = 'genres_update.html'
    success_url = reverse_lazy('genres-list')

class SeriaDetail(DetailView):
    model = Series

class SeriaDelete(DeleteView):
    model = Series
    success_url = reverse_lazy('series-list')

class SeriaList(ListView):
    model = Series

class SeriaCreate(CreateView):
    model = Series
    fields = ('name', 'descpiption')
    success_url = reverse_lazy('series-list')

class SeriaUpdate(UpdateView):
    model = Series
    fields = ('name', 'descpiption')
    template_name = 'series_update.html'
    success_url = reverse_lazy('series-list')

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
    template_name = 'publishers_update.html'
    success_url = reverse_lazy('publishers-list')