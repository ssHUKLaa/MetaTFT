from django.db import models

class Players(models.Model):
    autoinc=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    playerId = models.CharField(max_length=200)
    LP = models.IntegerField(default=0)
    add_date = models.DateTimeField('date added')