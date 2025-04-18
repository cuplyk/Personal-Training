from django.urls import path
from . import views
from django.shortcuts import render
from .views import CoachDashboardView, AthleteDashboardView, AddAthleteView, RemoveAthleteView, home

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL to the 'home' view
    # Map the dashboard URLs to their respective views
    path('coach/dashboard/', CoachDashboardView.as_view(), name='coach_dashboard'),
    path('athlete/dashboard/', AthleteDashboardView.as_view(), name='athlete_dashboard'),
    path('coach/add-athlete/<int:athlete_id>/', AddAthleteView.as_view(), name='add_athlete'),
    path('coach/remove-athlete/<int:athlete_id>/', RemoveAthleteView.as_view(), name='remove_athlete'),

]