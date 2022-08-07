from django.db.models import Q
from django.views.generic import ListView, TemplateView

from main.models import League, Match, Standing, Team


class HomeView(ListView):
    model = Team
    template_name = "main/home.html"
    context_object_name = 'suggest_teams'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        # set API's Team Name
        suggest_team_names = ['Liverpool FC', 'Manchester City FC', 'FC Barcelona', 'Real Madrid CF', 'AC Milan', 'FC Internazionale Milano', 'FC Bayern M\u00fcnchen', 'Borussia Dortmund']
        queryset = queryset.filter(Q(name=suggest_team_names[0]) | Q(name=suggest_team_names[1]) | Q(name=suggest_team_names[2]) | Q(name=suggest_team_names[3]) | Q(name=suggest_team_names[4]) | Q(name=suggest_team_names[5]) | Q(name=suggest_team_names[6]) | Q(name=suggest_team_names[7]))
        return queryset

class LeagueView(TemplateView):
    template_name = 'main/league.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league_code = self.kwargs.get('league_code')
        context['league'] = League.objects.get(code=league_code)
        context['matches'] = Match.objects.filter(home__league__code=league_code)[:10]
        context['standings'] = Standing.objects.filter(league__code=league_code)[:10]
        context['teams'] = Team.objects.filter(league__code=league_code)    
        return context


class ScheduleView(ListView):
    context_object_name = 'matches'
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


class StandingView(ListView):
    context_object_name = 'standings'
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


class MypageView(TemplateView):
    template_name = 'main/mypage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context