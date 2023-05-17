from django.db import models

class searchPlayers(models.Model):
    name = models.CharField(max_length=200,default='')
    playerId = models.CharField(max_length=200)
    LP = models.IntegerField(default=0)
    add_date = models.DateTimeField('date added')
    
class Matches(models.Model):
    otherParticipants = models.CharField(max_length=200, default='')
    traits = models.CharField(max_length=200, default='') #will have to delineate with commas
    placement = models.IntegerField(default=0)
    game_time = models.CharField(max_length=20, default='')

    searchedPlayer= models.ForeignKey(searchPlayers, on_delete=models.CASCADE,default=None)

class Champions(models.Model):
    Name = models.CharField(max_length=20, default='')
    Star = models.IntegerField(default=1)
    Items = models.CharField(max_length=100, default='') #will have to delineate with commas

    associatedMatch = models.ForeignKey(Matches,on_delete=models.CASCADE,default=None)
# Create your models here.
