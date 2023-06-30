from .models import Players
from django.utils import timezone
from topplayers.withriotapi import getChallengerPlayers, getGrandMasterPlayers, getMasterPlayers
import pytz

def getPlayers():
    return Players

def cron_reloadbest():
    total_entries = 0
    time = timezone.now()

    try:
        hold = getChallengerPlayers()
        x=0
        while total_entries <= 150:
            loadintoDB(hold, time, x, total_entries)
            x += 1
            total_entries += 1
    except:
        print('swag')
        try:
            hold = getGrandMasterPlayers()
            x = 0
            while total_entries <= 150:
                loadintoDB(hold, time, x, total_entries)
                x += 1
                total_entries += 1
        except:
            print('nahhh')
            try:
                hold = getMasterPlayers()
                x = 0
                while total_entries <= 150:
                    loadintoDB(hold, time, x, total_entries)
                    x += 1
                    total_entries += 1
            except:
                print("Error")

def loadintoDB(whichplayers, time, x, totalentries):
    b = Players()
    b.autoinc=totalentries
    b.name=str(list(dict(list(whichplayers.values())[x]).values())).strip("[]'")
    b.playerId=str(list(dict(list(whichplayers.values())[x]).keys())).strip("[]'")
    b.LP=list(whichplayers.keys())[x]
    b.add_date=time
    b.save()