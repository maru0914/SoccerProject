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

    **Context:**

    ``five_standings``
        A list of five_standings info.
    ``last_match``
        A dict of last match info.
    ``next_five_matches``
        A list of next 5 matches info.
    ``team``
        An instance of :model:`main.Team`.

    **Template:**

    :template:`mypage/dashboard.html`
    """
    template_name = 'mypage/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO : get team id from user table.(specific login user)
        team_id = 59
        team = Team.objects.get(id=team_id)
        context['team'] = team

        next_five_matches = []
        coming_matches = Match.objects.filter(
            (Q(home=team_id) | Q(away=team_id)) & Q(date__gte=datetime.now()))
        for i, match in enumerate(coming_matches):
            match_info = {}
            match_info['date'] = match.date
            match_info['match_day'] = match.match_day
            if match.home.id == team_id:
                match_info['opponent'] = match.away.name
            else:
                match_info['opponent'] = match.home.name
            next_five_matches.append(match_info)
            if i == 4:
                break
        context['next_five_matches'] = next_five_matches
        context['five_standings'] = self.get_five_standings(team)

        last_match = {}
        match= Match.objects.filter(
            (Q(home=team_id) | Q(away=team_id)) & Q(date__lte=datetime.now())).last()
        last_match['date'] = match.date
        if match.home.id == team_id:
            last_match['opponent'] = match.away.name
            team_score = match.home_score
            opponent_score = match.away_score
        else:
            last_match['opponent'] = match.home.name
            team_score = match.away_score
            opponent_score = match.home_score
        if team_score > opponent_score:
            last_match['result'] = 'win'
        elif team_score < opponent_score:
            last_match['result'] = 'lose'
        else:
            last_match['result'] = 'draw'
        last_match['home_score'] = match.home_score
        last_match['away_score'] = match.away_score

        context['last_match'] = last_match

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
