# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, CoachProfile, AthleteProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_coach = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_coach']

class CoachProfileForm(forms.ModelForm):
    class Meta:
        model = CoachProfile
        fields = ['bio', 'certifications', 'years_of_experience', 'specialties']

class AthleteProfileForm(forms.ModelForm):
    class Meta:
        model = AthleteProfile
        fields = ['height', 'weight', 'fitness_level']