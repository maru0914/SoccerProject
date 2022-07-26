from django.db.models import Q
from django.views.generic import ListView, TemplateView

from main.models import League, Match, Standing, Team


class HomeView(ListView):
    model = League
    template_name = "main/home.html"


class ScheduleView(ListView):
    model = Match
    paginate_by = 10
    template_name = "main/schedule.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get('key')
        if key == 'all':
            pass
        elif key.isdigit():
            team_id = int(key)
            context['team'] = Team.objects.get(id=team_id)
        else:
            league_code = key
            context['team_list'] = Team.objects.filter(league__code=league_code)
            context['league'] = League.objects.get(code=league_code)
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        key = self.kwargs.get('key')
        if key == 'all':
            pass
        elif key.isdigit():
            team_id = int(key)
            queryset = queryset.filter(Q(home=team_id) | Q(away=team_id))
        else:
            league_code = key
            queryset = queryset.filter(home__league__code=league_code)
        return queryset


class LeagueView(TemplateView):
    template_name = 'main/league.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league_code = self.kwargs.get('league_code')
        context['league'] = League.objects.get(code=league_code)
        context['teams'] = Team.objects.filter(league__code=league_code)    
        return context


class StandingView(ListView):
    model = Standing
    template_name = 'main/standing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league_code = self.kwargs.get('league_code')
        context['league'] = League.objects.get(code=league_code)
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        league_code = self.kwargs.get('league_code')
        queryset = queryset.filter(league__code=league_code)
        return queryset