from django import template 

from main.models import League

register = template.Library()

@register.filter
def league_to_ja(name):
    league = League.objects.get(name=name)
    japanese_name = league.leaguejapanese.name
    return japanese_name