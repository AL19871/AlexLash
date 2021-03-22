from django.urls import path
from customer import views

app_name = 'customer'

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile-update/', views.SubmitCustomer.as_view(), name='profile-update'),
    path('registration/', views.RegistrationView.as_view(), name = 'registration'),
    path('profile-list/', views.UserProfileList.as_view(), name='profile-list'),
    path('profile-upd/<int:pk>/', views.UserProfileUpdateManager.as_view(), name='profile-update-manager'),
    path('profile-delete/<int:pk>/', views.UserProfileDelete.as_view(), name='profile-delete')
]