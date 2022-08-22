"""Views for mypage app.
It's implemented by Class Based View.
"""
from datetime import datetime

from django.db.models import Q
from django.views.generic import TemplateView

from main.models import Match, Standing, Team


class DashboardView(TemplateView):
    """
    Display an dashboard for specific user.

    **Template:**

    :template:'mypage/dashboard.html'

    **Context:**

    :context: {
        'team': team,
        'next_five_matches': next_five_matches,
        'five_standings': five_standings,
        'last_match': last_match,
        'last_match_against': last_match_against
    }
    """
    template_name = 'mypage/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO : get team id from user table.(specific login user)
        team_id = 59
        team = Team.objects.get(id=team_id)
        context['team'] = team
        print(type(team))
        next_five_matches = []

        coming_matches = Match.objects.filter(
            (Q(home=team_id) | Q(away=team_id)) & Q(date__gte=datetime.now()))
        for i, match in enumerate(coming_matches):
            match_info = {}
            match_info['date'] = match.date
            match_info['match_day'] = match.match_day
            match_info['against'] = match.away.name if match.home.id == team_id else match.home.name
            next_five_matches.append(match_info)
            if i == 4:
                break
        context['next_five_matches'] = next_five_matches
        context['five_standings'] = self.get_five_standings(team)
        last_match= Match.objects.filter(
            (Q(home=team_id) | Q(away=team_id)) & Q(date__lte=datetime.now())).last()
        context['last_match'] = last_match
        if last_match.home.id == team_id:
            context['last_match_against'] = last_match.away.name
        else:
            context['last_match_against'] = last_match.home.name

        return context

    def get_five_standings(self, team):
        """get standings of 5 surrounding team

        Args:
            team (Team): team object

        Returns:
            standings: list of standings. (5 items surrounding args team)
        """
        rank = team.standing_set.first().rank
        if rank == 1:
            view_ranks = range(rank, rank + 5)
        elif rank == 2:
            view_ranks = range(rank - 1, rank + 4)
        elif rank == 3:
            view_ranks = range(rank - 2, rank + 3)
        elif rank == 4:
            view_ranks = range(rank - 3, rank + 2)
        elif rank == 5:
            view_ranks = range(rank - 4, rank + 1)
        league_standings = Standing.objects.filter(league__name=team.league.name)
        five_standings = []
        for standing in league_standings:
            if standing.rank in view_ranks:
                five_standings.append(standing)
        return five_standings
