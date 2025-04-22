from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from .models import CoachAthleteRelationship
from core.decorators import coach_required, athlete_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "index_x.html" )



class AddAthleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_coach

    def post(self, request, athlete_id):
        athlete = User.objects.get(id=athlete_id, is_athlete=True)
        CoachAthleteRelationship.objects.get_or_create(
            coach=request.user,
            athlete=athlete
        )
        return redirect('coach_dashboard')

class RemoveAthleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_coach

    def post(self, request, athlete_id):
        relationship = CoachAthleteRelationship.objects.get(
            coach=request.user,
            athlete__id=athlete_id
        )
        relationship.delete()
        return redirect('coach_dashboard')



@method_decorator(coach_required, name='dispatch')
class CoachDashboardView(View):
    def get(self, request):
        athletes = request.user.athletes.all()
        return render(request, 'dashboard_v2.html', {'athletes': athletes})

@method_decorator(athlete_required, name='dispatch')
class AthleteDashboardView(View):
    def get(self, request):
        coaches = request.user.coaches.all()
        return render(request, 'athlete_dashboard.html', {'coaches': coaches})