from django.views.generic import TemplateView

from main import get_info


class HomeView(TemplateView):
    template_name = "main/home.html"


class LeagueView(TemplateView):
    template_name = "main/league.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league_code = self.kwargs.get('league_code')
        context['team_list'] = get_info.get_team_list(league_code)
        context['league_code'] = league_code

        return context


class TeamView(TemplateView):
    template_name = "main/team.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league_code = self.kwargs.get('league_code')
        team_id = self.kwargs.get('id')
        context['match_list'] = get_info.get_match_list(league_code, team_id)
        context['league_code'] = league_code
        context['team_name'] = get_info.get_team_name_from_id(league_code, team_id)
        return context
