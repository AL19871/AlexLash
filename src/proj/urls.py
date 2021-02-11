"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_page, name = 'books-list'),

    path('autors/', views.AutorList.as_view(), name = 'autors-list'),
    path('autors-detail/<int:pk>/', views.AutorDetail.as_view(), name = 'autor-detail'),
    path('autors-delete/<int:pk>/', views.AutorDelete.as_view(), name = 'autor-delete'),
    path('autors-create/', views.AutorCreate.as_view(), name = 'autor-create'),
    path('autors-update/<int:pk>/', views.AutorUpdate.as_view(), name = 'autor-update'),

    path('genres/', views.GenreList.as_view(), name = 'genres-list'),
    path('genres-detail/<int:pk>/', views.GenreDetail.as_view(), name = 'genre-detail'),
    path('genres-delete/<int:pk>/', views.GenreDelete.as_view(), name = 'genre-delete'),
    path('genres-create/', views.GenreCreate.as_view(), name = 'genre-create'),
    path('genres-update/<int:pk>/', views.GenreUpdate.as_view(), name = 'genre-update'),

    path('publishers/', views.PublisherList.as_view(), name = 'publishers-list'),
    path('publishers-detail/<int:pk>/', views.PublisherDetail.as_view(), name = 'publisher-detail'),
    path('publishers-delete/<int:pk>/', views.PublisherDelete.as_view(), name = 'publisher-delete'),
    path('publishers-create/', views.PublisherCreate.as_view(), name = 'publisher-create'),
    path('publishers-update/<int:pk>/', views.PublisherUpdate.as_view(), name = 'publisher-update')
]
