from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CoachProfile, AthleteProfile

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_coach', 'is_athlete')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('is_coach', 'is_athlete', 'phone_number', 'date_of_birth')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(CoachProfile)
admin.site.register(AthleteProfile)