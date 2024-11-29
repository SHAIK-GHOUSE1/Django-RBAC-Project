from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from functools import wraps


def role_required(allowed_roles):
    """
    Custom decorator to restrict access based on user role.
    `allowed_roles` is a list of roles that can access the view.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user is authenticated
            if not request.user.is_authenticated:
                return redirect("login")  # Redirect to login page if not authenticated

            # Check if the user has a role attribute
            if not hasattr(request.user, "role"):
                return HttpResponseForbidden("User role is not defined.")

            # Check if the user's role is in the allowed roles
            if request.user.role not in allowed_roles:
                return HttpResponseForbidden(
                    "You do not have the required permissions."
                )

            # Proceed with the view if all checks pass
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
