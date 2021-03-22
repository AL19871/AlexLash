from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('checkout/', views.DetailOrder.as_view(), name='checkout'),
    path('checkout-submit/', views.SubmitOrder.as_view(), name='order-submit'),
    path('order-list/', views.OrdersList.as_view(), name='order-list'),
    path('order-update/<int:pk>/', views.OrderUpdateView.as_view(), name='order-update'),
    path('order-detail/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order-delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order-delete')
]