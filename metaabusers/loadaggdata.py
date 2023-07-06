from topplayers.withriotapi import getPlayer, getMatches, getMatch
from .models import Players, AggregateData
from concurrent.futures import ThreadPoolExecutor
from .rebestplayer import cron_reloadbest
from django.utils import timezone
import time

def loadaggdata():
    count=Players.objects.count()
    UseDB=False
    if count>=1:
        
        getAll= Players.objects.all()
        getFirst=getAll.first()
        adddate = getFirst.add_date
        nowtime=timezone.now()
        timediff = nowtime-adddate
        if ((timediff.days)<=2):
            UseDB = True

        if UseDB==True:
            for player in getAll:
                playerstuff=getPlayer(player.name)
                allMatches=getMatches(playerstuff)
                processmatches(playerstuff,allMatches)
                time.sleep(5)
    else: 
        cron_reloadbest()
        loadaggdata()


def processmatches(playerstuff, allMatches):
    
    def processmatch(inc):
        print('swag')
        tes = getMatch(allMatches,inc)
        
        playerpuuid=(playerstuff.get('puuid'))
        lamo = ((tes.get('info')).get('participants'))

        inc2 = 0
        for eachpl in lamo:
            if (playerpuuid==(eachpl.get('puuid'))):
                break
            inc2+=1
        
        unitlist = lamo[inc2].get('units')

        inc3=0
        for unit in unitlist:
            useName=(unit.get('character_id'))
            newaggentry=AggregateData()
            newaggentry.id=allMatches[inc]+(','+str(inc3))
            newaggentry.Name=useName.lower()
            newaggentry.Star=unit.get('tier')
            newaggentry.Items=','.join(unit.get('itemNames'))
            newaggentry.Augments=','.join((lamo[inc2]).get('augments'))
            newaggentry.save()
            inc3+=1
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(processmatch, range(len(allMatches)))
