from rest_framework import permissions
from .exceptions import LogInvalidationError

class IsLoggedIn(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        raise LogInvalidationError("User is not authenticated.")