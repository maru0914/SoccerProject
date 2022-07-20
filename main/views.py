from django.views.generic import TemplateView

from main import get_info



class HomeView(TemplateView):
    template_name = "main/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['match_list'] = get_info.test_get_info_from_json()
        return context


class LeagueView(TemplateView):
    template_name = "main/league.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league_name = self.kwargs.get('league')
        context['team_list'] = get_info.get_team_list(league_name)
        context['league_name'] = league_name

        return context