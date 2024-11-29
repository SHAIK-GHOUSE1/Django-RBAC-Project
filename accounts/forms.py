from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)  # Import Django's built-in forms for user creation and authentication
from .models import CustomUser  # Import the custom user model


# Custom user creation form to handle registration of new users
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use the custom user model
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "role",
        ]  # Specify the fields to be included in the form


# Custom authentication form for logging in existing users
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser  # Use the custom user model for authentication
        fields = [
            "username",
            "password",
        ]  # Specify the fields to be included in the form
