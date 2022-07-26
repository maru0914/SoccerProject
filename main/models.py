from django.db import models


class League(models.Model):
    code = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=40)
    emblem = models.URLField(max_length=200, null=True)

    class Meta:
        db_table = 'league'


class LeagueJapanese(models.Model):
    league = models.OneToOneField(League, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'league_japanese'


class Team(models.Model):
    name = models.CharField(max_length=40)
    crest = models.URLField(max_length=200, null=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    class Meta:
        db_table = 'team'
        constraints = [models.UniqueConstraint(fields=['name', 'league'], name='unique_team')]

class TeamJapanese(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'team_japanese'


class Season(models.Model):
    year = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    class Meta:
        db_table = 'season'
        constraints = [models.UniqueConstraint(fields=['year', 'league'], name='unique_season')]


class Match(models.Model):
    date = models.DateTimeField()
    match_day = models.PositiveIntegerField()
    home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    class Meta:
        db_table = 'match'
        constraints = [models.UniqueConstraint(fields=['match_day', 'home', 'away', 'season'], name='unique_match')]
        ordering = ['date']


class Standing(models.Model):
    rank = models.PositiveIntegerField(null=True)
    point = models.PositiveIntegerField()
    played = models.PositiveIntegerField()
    won = models.PositiveIntegerField()
    draw = models.PositiveIntegerField()
    lost = models.PositiveIntegerField()
    goals_for = models.PositiveIntegerField()
    goals_against = models.PositiveIntegerField()
    goals_difference = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    class Meta:
        db_table = 'standing'
        constraints = [models.UniqueConstraint(fields=['team', 'league'], name='unique_standing')]
        ordering = ['rank']