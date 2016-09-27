from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Player(models.Model):
    PlayerID = models.CharField(max_length=20, primary_key=True)
    PlayerName = models.CharField(max_length=100)
    DOB = models.DateField()

class Match(models.Model):
    MatchID = models.IntegerField(primary_key=True)
    TeamID1 = models.IntegerField()
    TeamID2 = models.IntegerField()
    SeriesID = models.IntegerField()
    GroundID = models.IntegerField()
    MDate = models.DateField()
    Umpire = models.CharField(max_length=10)

class PlayerMatch(models.Model):
    PlayerID = models.ForeignKey(Player, on_delete=models.CASCADE)
    MatchID = models.ForeignKey(Match, on_delete=models.CASCADE)
    Fours = models.IntegerField(null=True)
    Sixes = models.IntegerField(null=True)
    TotalRuns = models.IntegerField(null=True)
    Catches = models.IntegerField(null=True)
    Wickets = models.IntegerField(null=True)
    Overs = models.IntegerField(null=True)
    Type = models.CharField(max_length=5)
    Strategy = models.CharField(max_length=10, null=True)

class Team(models.Model):
    TeamID = models.IntegerField(primary_key=True)
    HostGroundID = models.IntegerField(null=True)
    Coach = models.CharField(max_length=20, null=True)

class PlayerTeam(models.Model):
    PlayerID = models.ForeignKey(Player, on_delete=models.CASCADE)
    TeamID = models.ForeignKey(Team, on_delete=models.CASCADE)

class Ground(models.Model):
    GroundID = models.IntegerField(primary_key=True)
    GroundType = models.CharField(max_length=20)
    PitchType = models.CharField(max_length=20)

class Series(models.Model):
    SeriesID = models.IntegerField(primary_key=True)
    GroundID = models.ForeignKey(Ground, on_delete=models.CASCADE)
    ManOfTheSeries = models.IntegerField()






 
