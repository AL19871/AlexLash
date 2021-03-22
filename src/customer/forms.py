from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserDetailsForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'last_name', 'first_name')