# core/decorators.py
from django.core.exceptions import PermissionDenied
from functools import wraps
from django.shortcuts import redirect

# Decorators to check if the user is a coach or an athlete
# These decorators can be used to restrict access to certain views based on the user's role
def coach_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_coach:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def athlete_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_athlete:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view