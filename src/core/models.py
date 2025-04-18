# training_service/models.py
from django.db import models
from users.models import User

class CoachAthleteRelationship(models.Model):
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='athletes')
    athlete = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coaches')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('coach', 'athlete')