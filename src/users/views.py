# users/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, CoachProfileForm, AthleteProfileForm
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'auth/login_x.html', {'form': form})
    ## Handle the login process
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

# users/views.py
class RegisterView(View):
    def get(self, request):
        user_form = UserRegisterForm()
        coach_form = CoachProfileForm()
        athlete_form = AthleteProfileForm()
        return render(request, 'auth/register.html', {
            'user_form': user_form,
            'coach_form': coach_form,
            'athlete_form': athlete_form
        })
    ## Handle the registration process
    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        coach_form = CoachProfileForm(request.POST)
        athlete_form = AthleteProfileForm(request.POST)
        ## Handle the registration process
        if user_form.is_valid():
            user = user_form.save(commit=False)
            is_coach = user_form.cleaned_data.get('is_coach')
            
            if is_coach and coach_form.is_valid():
                user.is_coach = True
                user.save()
                coach_profile = coach_form.save(commit=False)
                coach_profile.user = user
                coach_profile.save()
                return redirect('coach_profile_complete')
            elif not is_coach and athlete_form.is_valid():
                user.is_athlete = True
                user.save()
                athlete_profile = athlete_form.save(commit=False)
                athlete_profile.user = user
                athlete_profile.save()
                return redirect('athlete_profile_complete')
         ## If the forms are not valid, render the registration page again with errors       
        return render(request, 'auth/register.html', {
            'user_form': user_form,
            'coach_form': coach_form,
            'athlete_form': athlete_form
        })

# Check if username is available
def check_username(request):
    username = request.GET.get('username', '')
    User = get_user_model()
    data = {
        'available': not User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


class CoachProfileCompleteView(View):
    def get(self, request):
        if not request.user.is_coach:
            return redirect('home')
        form = CoachProfileForm(instance=request.user.coachprofile)
        return render(request, 'dashboard.html', {'form': form})

    def post(self, request):
        form = CoachProfileForm(request.POST, instance=request.user.coachprofile)
        if form.is_valid():
            form.save()
            return redirect('coach_dashboard')
        return render(request, 'dashboard.html', {'form': form})

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