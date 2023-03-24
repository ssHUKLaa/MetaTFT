from django.db import models


class Players(models.Model):
    name = models.CharField(max_length=200)
    playerId = models.CharField(max_length=200)
    LP = models.IntegerField(default=0)
    add_date = models.DateTimeField('date added')

class searchPlayers(models.Model):
    name = models.CharField(max_length=200)
    playerId = models.CharField(max_length=200)
    LP = models.IntegerField(default=0)
    add_date = models.DateTimeField('date added')

class Matches(models.Model):
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    searchedPlayer = models.ForeignKey(searchPlayers, on_delete=models.CASCADE)

# Create your models here.
