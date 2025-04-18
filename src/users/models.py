# filepath: /workspaces/Personal-Training/src/users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    is_coach = models.BooleanField(default=False)
    is_athlete = models.BooleanField(default=False)  # Corretto il typo

    # common fields for both tipes of users
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
class CoachProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coach_profile')
    bio = models.TextField(blank=True)
    years_of_experience = models.IntegerField(default=0)
    certifications = models.TextField(blank=True)   
    specialties = models.TextField(blank=True)

class AthleteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='athlete_profile')
    bio = models.TextField(blank=True)
    goals = models.TextField(blank=True)
    height = models.FloatField(blank=True, null=True)  # in cm
    weight = models.FloatField(blank=True, null=True) # in kg
    fitness_level = models.CharField(max_length=50, blank=True)

