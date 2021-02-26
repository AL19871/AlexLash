from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginIn.as_view(), name = 'my-login'),
    path('logout/', views.LoginOut.as_view(), name = 'my-logout')
]