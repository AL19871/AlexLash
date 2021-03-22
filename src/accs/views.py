from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView

class LoginIn(LoginView):
    success_url = reverse_lazy('home-page')


class LoginOut(LogoutView):
    template_name = 'registration/my_logged_out.html'
