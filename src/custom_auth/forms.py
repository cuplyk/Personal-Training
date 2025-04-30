from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, 
    PasswordResetForm, 
    SetPasswordForm
)

class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False, 
        initial=True,
        widget=forms.CheckboxInput()
    )

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    