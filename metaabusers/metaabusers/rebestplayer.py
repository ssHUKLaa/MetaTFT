from .models import Players
from django.utils import timezone
from topplayers.withriotapi import getChallengerPlayers
import pytz

def cron_reloadbest():
    x=0
    hold=getChallengerPlayers()
    time=timezone.now()
    try:
        while x<150:
            b = Players()
            b.autoinc=x
            b.name=str(list(dict(list(hold.values())[x]).values())).strip("[]'")
            b.playerId=str(list(dict(list(hold.values())[x]).keys())).strip("[]'")
            b.LP=list(hold.keys())[x]
            b.add_date=time
            x+=1
            b.save()
    except:
        print("error")