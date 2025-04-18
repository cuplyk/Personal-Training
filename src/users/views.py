# users/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, CoachProfileForm, AthleteProfileForm
from django.views import View

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'auth/login_x.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_coach:
                return redirect('coach_dashboard')
            else:
                return redirect('athlete_dashboard')
        return render(request, 'auth/login_x.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class RegisterView(View):
    def get(self, request):
        user_form = UserRegisterForm()
        return render(request, 'users/register.html', {'user_form': user_form})

    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            is_coach = user_form.cleaned_data.get('is_coach')
            
            if is_coach:
                user.is_coach = True
            else:
                user.is_athlete = True
                
            user.save()
            
            # Create profile
            if is_coach:
                CoachProfile.objects.create(user=user)
                return redirect('coach_profile_complete')
            else:
                AthleteProfile.objects.create(user=user)
                return redirect('athlete_profile_complete')
                
        return render(request, 'users/register.html', {'user_form': user_form})



class CoachProfileCompleteView(View):
    def get(self, request):
        if not request.user.is_coach:
            return redirect('home')
        form = CoachProfileForm(instance=request.user.coachprofile)
        return render(request, 'users/coach_profile_complete.html', {'form': form})

    def post(self, request):
        form = CoachProfileForm(request.POST, instance=request.user.coachprofile)
        if form.is_valid():
            form.save()
            return redirect('coach_dashboard')
        return render(request, 'users/coach_profile_complete.html', {'form': form})

class AthleteProfileCompleteView(View):
    def get(self, request):
        if not request.user.is_athlete:
            return redirect('home')
        form = AthleteProfileForm(instance=request.user.athleteprofile)
        return render(request, 'users/athlete_profile_complete.html', {'form': form})

    def post(self, request):
        form = AthleteProfileForm(request.POST, instance=request.user.athleteprofile)
        if form.is_valid():
            form.save()
            return redirect('athlete_dashboard')
        return render(request, 'users/athlete_profile_complete.html', {'form': form})