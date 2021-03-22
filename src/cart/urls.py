from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('add-to-cart/', views.DetailCart.as_view(), name='add-to-cart'),
    path('recalculate-to-cart/', views.RecalculateCart.as_view(), name='recalculate-to-cart')
]