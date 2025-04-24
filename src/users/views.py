from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from .forms import (
    UserRegisterForm, 
    UserUpdateForm,
    CoachProfileForm,
    AthleteProfileForm
)

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_coach = form.cleaned_data.get('is_coach', False)
            user.is_athlete = not user.is_coach
            user.save()
            
            if user.is_coach:
                return redirect('coach_profile_complete')
            return redirect('athlete_profile_complete')
        return render(request, 'users/register.html', {'form': form})

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        
        if request.user.is_coach:
            profile_form = CoachProfileForm(instance=request.user.coachprofile)
        else:
            profile_form = AthleteProfileForm(instance=request.user.athleteprofile)
            
        return render(request, 'users/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request):
        user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        
        if request.user.is_coach:
            profile_form = CoachProfileForm(request.POST, instance=request.user.coachprofile)
        else:
            profile_form = AthleteProfileForm(request.POST, instance=request.user.athleteprofile)
            
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
            
        return render(request, 'users/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })