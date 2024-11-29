from django.shortcuts import render, redirect  # Import render and redirect functions
from django.contrib.auth import (
    login,
    logout,
    authenticate,
)  # Import login, logout, and authenticate functions
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
)  # Import the custom forms
from .utils import role_required  # Import the role-based decorator


# Register view for handling user registration
def register(request):
    if request.method == "POST":  # If the form has been submitted
        form = CustomUserCreationForm(
            request.POST
        )  # Create a form instance with submitted data
        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the new user to the database
            return redirect(
                "home"
            )  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()  # If GET request, create an empty form
    return render(
        request, "accounts/register.html", {"form": form}
    )  # Render the registration page with the form


# Login view for handling user login
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect based on user role
            if user.role == "Admin":
                return redirect("admin_dashboard")
            elif user.role == "Moderator":
                return redirect("moderator_dashboard")
            elif user.role == "User":
                return redirect("user_dashboard")
            else:
                return redirect("home")  # Default redirection

    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


# Logout view for handling user logout
def logout_view(request):
    logout(request)  # Log the user out
    return redirect("home")  # Redirect to the login page after logging out


# Admin dashboard view
@role_required(["Admin"])
def admin_dashboard(request):
    return render(request, "accounts/admin_dashboard.html", {"role": "Admin"})


# User dashboard view
@role_required(["User"])
def user_dashboard(request):
    return render(request, "accounts/user_dashboard.html", {"role": "User"})


# Moderator dashboard view
@role_required(["Moderator"])
def moderator_dashboard(request):
    return render(request, "accounts/moderator_dashboard.html", {"role": "Moderator"})


# accounts/utils.py
from django.http import HttpResponseForbidden
from functools import wraps


def role_required(allowed_roles):
    """
    Custom decorator to restrict access based on user role.
    `allowed_roles` is a list of roles that can access the view.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role not in allowed_roles:
                return HttpResponseForbidden(
                    "You are not authorized to view this page."
                )
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


def home(request):
    return render(request, "accounts/home.html")
