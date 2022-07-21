from django.db import models


class League(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'league'


class LeagueJapanese(models.Model):
    league = models.OneToOneField(League, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'league_japanese'


class Team(models.Model):
    name = models.CharField(max_length=40)
    crest = models.URLField(max_length=200)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    class Meta:
        db_table = 'team'


class TeamJapanese(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'team_japanese'


class Match(models.Model):
    date = models.DateTimeField()
    match_day = models.PositiveIntegerField()
    home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')

    class Meta:
        db_table = 'match'