# auth/adapter.py
from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse
from django import forms

class RoleAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        
        # Get role from form (you'll need to customize your signup form)
        role = form.cleaned_data.get('role', 'athlete')
        
        if role == 'coach':
            user.is_coach = True
        else:
            user.is_athlete = True
            
        if commit:
            user.save()
        return user

    def get_login_redirect_url(self, request):
        # Custom redirect based on user role
        if request.user.is_coach:
            return reverse('coach_dashboard')
        return reverse('athlete_dashboard')