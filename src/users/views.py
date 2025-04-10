from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to the home page
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})