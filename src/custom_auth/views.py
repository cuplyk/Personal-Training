from django.contrib.auth import login, logout
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, CustomPasswordResetForm, CustomSetPasswordForm

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if not form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)  # Session expires when browser closes
            
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
                
            if user.is_coach:
                return redirect('coach_dashboard')
            return redirect('athlete_dashboard')
        return render(request, 'auth/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'auth/logout.html')

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'auth/password_reset/form.html'
    email_template_name = 'auth/password_reset/email.html'
    subject_template_name = 'auth/password_reset/subject.txt'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'auth/password_reset/done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'auth/password_reset/confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'auth/password_reset/complete.html'