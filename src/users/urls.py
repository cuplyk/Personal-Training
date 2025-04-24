# users/urls.py
from django.urls import path
from .views import RegisterView, ProfileView
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    #path('coach/profile/complete/', CoachProfileCompleteView.as_view(), name='coach_profile_complete'),
    #path('athlete/profile/complete/', AthleteProfileCompleteView.as_view(), name='athlete_profile_complete'),

    # users/urls.py
    #path('api/check-username/', views.check_username, name='check_username'),
]

