from django.db import models

class searchPlayers(models.Model):
    name = models.CharField(max_length=200,default='')
    id = models.CharField(max_length=200,primary_key=True)
    LP = models.IntegerField(default=0)
    add_date = models.DateTimeField('date')
    
class Matches(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    otherParticipants = models.CharField(max_length=200, default='')
    placement = models.IntegerField(default=0)
    game_time = models.CharField(max_length=20, default='')
    game_length = models.CharField(max_length=20, default='')

    searchedPlayer= models.ForeignKey(searchPlayers, on_delete=models.CASCADE,default=None)

class Traits(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    traitname = models.CharField(max_length=100, default='')
    currenttier = models.IntegerField(default=0)
    tierunits = models.IntegerField(default=0)

    associatedMatch = models.ForeignKey(Matches,on_delete=models.CASCADE,default=None)

class Champions(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    Name = models.CharField(max_length=20, default='')
    Star = models.IntegerField(default=1)
    Items = models.CharField(max_length=100, default='') #will have to delineate with commas
    Rarity = models.IntegerField(default=0)

    associatedMatch = models.ForeignKey(Matches,on_delete=models.CASCADE,default=None)
# Create your models here.
