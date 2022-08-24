"""Views for mypage app.
"""
from datetime import datetime

from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView

from accounts.models import MyUser
from main.models import Match, Standing, Team


class DashboardView(View):
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

    def get(self, request):
        """get method for DashboardView"""
        context = {}
        if not self.request.user.favorite_team:
            return redirect('mypage:select_team')
        team_id = self.request.user.favorite_team.id
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
        if team_score is None:
            last_match['result'] = 'updating'
        else:
            if team_score > opponent_score:
                last_match['result'] = 'win'
            elif team_score < opponent_score:
                last_match['result'] = 'lose'
            else:
                last_match['result'] = 'draw'
        last_match['home_score'] = match.home_score
        last_match['away_score'] = match.away_score

        context['last_match'] = last_match

        return render(request, self.template_name, context)

    def get_five_standings(self, team):
        """get standings of 5 surrounding team

        Args:
            team (Team): team object

        Returns:
            standings: list of standings. (5 items surrounding args team)
        """
        rank = team.standing_set.first().rank
        league_code = team.league.code
        league_standings = Standing.objects.filter(league__name=team.league.name)
        bundes_lookup = {
            1: range(rank, rank + 5),
            2: range(rank - 1, rank + 4),
            17: range(rank - 3, rank + 2),
            18: range(rank - 4, rank + 1)
            }
        other_lookup = {
            1: range(rank, rank + 5),
            2: range(rank - 1, rank + 4),
            19: range(rank - 3, rank + 2),
            20: range(rank - 4, rank + 1)
            }
        if league_code == 'BL1':
            view_ranks = bundes_lookup.get(rank, range(rank-2, rank + 3))
        else:
            view_ranks = other_lookup.get(rank, range(rank-2, rank + 3))
        five_standings = []
        for standing in league_standings:
            if standing.rank in view_ranks:
                five_standings.append(standing)
        return five_standings


class SelectTeamView(ListView):
    """
    Display a list of teams.
    """
    template_name = 'mypage/select_team.html'
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        return Team.objects.all()

def register_team(request):
    """Register a favorite team."""
    user = MyUser.objects.get(id=request.user.id)
    data = request.POST
    favorite_team = data.get('selected-team')
    if not favorite_team:
        return redirect('mypage:select_team')
    user.favorite_team = Team.objects.get(id=favorite_team)
    user.save()
    return redirect('mypage:dashboard')
