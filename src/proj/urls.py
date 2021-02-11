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
    path('cities/', views.CityList.as_view(), name = 'cities-list'),
    path('cities-detail/<int:pk>/', views.CityDetail.as_view(), name = 'city-detail'),
    path('cities-delete/<int:pk>/', views.CityDelete.as_view(), name = 'city-delete'),
    path('cities-create/', views.CityCreate.as_view(), name = 'city-create'),
    path('cities-update/<int:pk>/', views.CityUpdate.as_view(), name = 'city-update')
]
