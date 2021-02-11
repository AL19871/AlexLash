from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView, UpdateView, CreateView
from books.models import Cities

class CityDetail(DetailView):
    model = Cities

class CityDelete(DeleteView):
    model = Cities
    success_url = reverse_lazy('cities-list')

class CityList(ListView):
    model = Cities

class CityCreate(CreateView):
    model = Cities
    fields = ('name',)
    success_url = reverse_lazy('cities-list')

class CityUpdate(UpdateView):
    model = Cities
    fields = ('name',)
    success_url = reverse_lazy('cities-list')