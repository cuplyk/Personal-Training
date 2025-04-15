# filepath: /workspaces/Personal-Training/src/users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('coach', 'Coach'),
        ('athlete', 'Athlete'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)