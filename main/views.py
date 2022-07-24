from django.db.models import Q
from django.views.generic import ListView, TemplateView

from main import get_info
from main.models import League, Match, Team


class HomeView(ListView):
    model = League
    template_name = "main/home.html"


class LeagueView(TemplateView):
    template_name = "main/league.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league_code = self.kwargs.get('league_code')
        context['team_list'] = Team.objects.filter(league__code=league_code)
        context['league_code'] = league_code
        return context


class TeamView(TemplateView):
    template_name = "main/team.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league_code = self.kwargs.get('league_code')
        team_id = self.kwargs.get('id')
        context['match_list'] = Match.objects.filter(Q(home=team_id) | Q(away=team_id))
        context['league_code'] = league_code
        context['team'] = Team.objects.get(id=team_id)
        return context
