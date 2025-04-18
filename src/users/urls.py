# users/urls.py
from django.urls import path
from .views import LoginView, LogoutView, RegisterView, CoachProfileCompleteView, AthleteProfileCompleteView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('coach/profile/complete/', CoachProfileCompleteView.as_view(), name='coach_profile_complete'),
    path('athlete/profile/complete/', AthleteProfileCompleteView.as_view(), name='athlete_profile_complete'),
]

