from django.db import models

class Players(models.Model):
    autoinc=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    playerId = models.CharField(max_length=200)
    LP = models.IntegerField(default=0)
    add_date = models.DateTimeField('date added')

class AggregateData(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    Name = models.CharField(max_length=20, default='')
    Star = models.IntegerField(default=1)
    Items = models.CharField(max_length=100, default='')
    Augments = models.CharField(max_length=100, default='')

