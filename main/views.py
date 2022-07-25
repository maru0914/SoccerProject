from django.db.models import Q
from django.views.generic import ListView

from main.models import League, Match, Team


class HomeView(ListView):
    model = League
    template_name = "main/home.html"


class ScheduleView(ListView):
    model = Match
    paginate_by = 10
    template_name = "main/schedule.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            team_id = int(self.kwargs.get('key'))
            context['team'] = Team.objects.get(id=team_id)

        except ValueError:
            league_code = self.kwargs.get('key')
            context['team_list'] = Team.objects.filter(league__code=league_code)
            context['league'] = League.objects.get(code=league_code)
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        try:
            team_id = int(self.kwargs.get('key'))
            queryset = queryset.filter(Q(home=team_id) | Q(away=team_id))
        except ValueError:
            league_code = self.kwargs.get('key')
            queryset = queryset.filter(home__league__code=league_code)
        return queryset
