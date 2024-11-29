from django.urls import path  # Import the path function for defining URL patterns
from .views import (  # Import all the necessary views
    register,
    login_view,
    logout_view,
    admin_dashboard,
    user_dashboard,
    moderator_dashboard,
)

# Define the URL patterns for the accounts app
urlpatterns = [
    # Authentication-related paths
    path("register/", register, name="register"),  # Registration page
    path("login/", login_view, name="login"),  # Login page
    path("logout/", logout_view, name="logout"),  # Logout action
    # Role-based dashboard paths
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("user-dashboard/", user_dashboard, name="user_dashboard"),
    path("moderator-dashboard/", moderator_dashboard, name="moderator_dashboard"),
]
