from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, CoachProfile, AthleteProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_coach = forms.BooleanField(
        required=False,
        label='Register as a coach'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_coach']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class CoachProfileForm(forms.ModelForm):
    class Meta:
        model = CoachProfile
        fields = ['specialties', 'certifications', 'years_of_experience']

class AthleteProfileForm(forms.ModelForm):
    class Meta:
        model = AthleteProfile
        fields = ['height', 'weight', 'fitness_level']