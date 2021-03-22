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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from books import views
from accs import urls as accs_urls
from cart import urls as cart_urls
from order import urls as order_urls
from customer import urls as customer_urls

urlpatterns = [

    path('', views.HomePage.as_view(), name = 'home-page'),

    path('s-admin/', admin.site.urls),

    path('books/', views.BookList.as_view(), name = 'books-list'),
    path('books-detail/<int:pk>/', views.BookDetail.as_view(), name = 'book-detail'),
    path('books-delete/<int:pk>/', views.BookDelete.as_view(), name = 'book-delete'),
    path('books-create/', views.BookCreate.as_view(), name = 'book-create'),
    path('books-update/<int:pk>/', views.BookUpdate.as_view(), name = 'book-update'),

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

    path('series/', views.SeriaList.as_view(), name = 'series-list'),
    path('series-detail/<int:pk>/', views.SeriaDetail.as_view(), name = 'seria-detail'),
    path('series-delete/<int:pk>/', views.SeriaDelete.as_view(), name = 'seria-delete'),
    path('series-create/', views.SeriaCreate.as_view(), name = 'seria-create'),
    path('series-update/<int:pk>/', views.SeriaUpdate.as_view(), name = 'seria-update'),

    path('addresses/', views.AddressList.as_view(), name = 'addresses-list'),
    path('addresses-detail/<int:pk>/', views.AddressDetail.as_view(), name = 'address-detail'),
    path('addresses-delete/<int:pk>/', views.AddressDelete.as_view(), name = 'address-delete'),
    path('addresses-create/', views.AddressCreate.as_view(), name = 'address-create'),
    path('addresses-update/<int:pk>/', views.AddressUpdate.as_view(), name = 'address-update'),

    path('cities/', views.CityList.as_view(), name = 'cities-list'),
    path('cities-detail/<int:pk>/', views.CityDetail.as_view(), name = 'city-detail'),
    path('cities-delete/<int:pk>/', views.CityDelete.as_view(), name = 'city-delete'),
    path('cities-create/', views.CityCreate.as_view(), name = 'city-create'),
    path('cities-update/<int:pk>/', views.CityUpdate.as_view(), name = 'city-update'),

    path('publishers/', views.PublisherList.as_view(), name = 'publishers-list'),
    path('publishers-detail/<int:pk>/', views.PublisherDetail.as_view(), name = 'publisher-detail'),
    path('publishers-delete/<int:pk>/', views.PublisherDelete.as_view(), name = 'publisher-delete'),
    path('publishers-create/', views.PublisherCreate.as_view(), name = 'publisher-create'),
    path('publishers-update/<int:pk>/', views.PublisherUpdate.as_view(), name = 'publisher-update')
]

urlpatterns.append(path('accs/', include(accs_urls)))
urlpatterns.append(path('cart/', include(cart_urls, namespace='cart')))
urlpatterns.append(path('order/', include(order_urls, namespace='order')))
urlpatterns.append(path('customer/', include(customer_urls, namespace='customer')))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)