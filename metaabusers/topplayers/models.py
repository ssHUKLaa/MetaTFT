from django.db import models

class Matches(models.Model):
    Participants = models.CharField(max_length=200)
    
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
    match= models.ForeignKey(Matches, on_delete=models.CASCADE)


    

# Create your models here.
