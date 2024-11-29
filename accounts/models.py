from django.contrib.auth.models import AbstractUser  # Import the base User model class
from django.db import models  # Import Django's model class to define database models


# Define a custom user model by extending AbstractUser
class CustomUser(AbstractUser):
    # Add a 'role' field to the custom user model to store the user's role
    role = models.CharField(
        max_length=50,  # Limit the length of the role string to 50 characters
        choices=[  # Define a list of possible roles a user can have
            ("Admin", "Admin"),  # Admin role with the label 'Admin'
            ("User", "User"),  # Regular User role with the label 'User'
            ("Moderator", "Moderator"),  # Moderator role with the label 'Moderator'
        ],
        default="User",  # Set the default role to 'User' if no role is specified
    )

    # Define a string representation method for the user model
    def __str__(self):
        # When we print a CustomUser instance, it will return the username
        return self.username
