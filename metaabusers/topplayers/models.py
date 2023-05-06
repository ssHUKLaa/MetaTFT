from django.db import models

class Matches(models.Model):
    Participants = models.CharField(max_length=200, default='')
    
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
    match= models.ForeignKey(Matches, on_delete=models.CASCADE,default=None)


    

# Create your models here.
