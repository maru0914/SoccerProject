from django import template 

from main.models import League, Team

register = template.Library()

@register.filter
def league_to_ja(name):
    league = League.objects.get(name=name)
    japanese_name = league.leaguejapanese.name
    return japanese_name

@register.filter
def team_to_ja(name):
    team = Team.objects.get(name=name)
    japanese_name = team.teamjapanese.name
    return japanese_name