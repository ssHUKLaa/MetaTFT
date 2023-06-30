from ..topplayers.withriotapi import getPlayer, getMatches, getMatch
from .models import Players, AggregateData
from concurrent.futures import ThreadPoolExecutor
from .rebestplayer import cron_reloadbest
from django.utils import timezone

def comparematchtoagg():
    UseDB=False
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
    else: 
        cron_reloadbest()
        comparematchtoagg()


def processmatches(playerstuff, allMatches):
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(processmatch, range(len(allMatches)))

    def processmatch(inc):
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
            Name=(unit.get('character_id'))
            newaggentry=AggregateData()
            newaggentry.id = allMatches[inc]+(','+inc3)
            newaggentry.Name = Name.lower()
            newaggentry.Star = unit.get('tier')
            newaggentry.Items = unit.get('itemNames')
            newaggentry.Augments = (lamo[inc2]).get('augments')
            newaggentry.save()
            inc3+=1
