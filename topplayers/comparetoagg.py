from ..metaabusers.models import Players
from .withriotapi import getPlayer, getMatches, getMatch
from django.utils import timezone

def comparematchtoagg(traits, champs):
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


def processmatches(playerstuff, allMatches):

    def processmatch(inc):
                    tes = getMatch(allMatches,inc)
                    
                    playerpuuid=(playerstuff.get('puuid'))
                    lamo = ((tes.get('info')).get('participants'))

                    inc2 = 0
                    for eachpl in lamo:
                        if (playerpuuid==(eachpl.get('puuid'))):
                            break
                        inc2+=1
                    traitlist=lamo[inc2].get('traits')
                    traits=[]
                    for trait in traitlist:
                        traitdict={'Name':(trait.get('name'))[5:].lower(),
                                'tier':trait.get('tier_current')
                                }
                        traits.append(traitdict)
                    
                    unitlist = lamo[inc2].get('units')
                    champs=[]

                    for unit in unitlist:
                        Name=(unit.get('character_id'))
                        champdict={'Name':Name.lower(),
                                'Star':unit.get('tier'),
                                'Items':unit.get('itemNames')
                        }
                        champs.append(champdict)


    