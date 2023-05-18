from .models import Matches, searchPlayers, Champions, Traits
from django.utils import timezone
from .withriotapi import searchPlayerStuff, getMatches, getMatch, nameByPUUID

def fillDb(player):
    time=timezone.now()

    x = searchPlayerStuff(player.get('id'))
    if (x==False):
        b=searchPlayers()
        b.name=(player.get('name'))
        b.playerId=(player.get('id'))
        b.LP=-1
        b.add_date=timezone.now()
        b.save()
    b=searchPlayers()
    b.name=(player.get('name'))
    b.playerId=(player.get('id'))
    b.LP=-1
    b.add_date=timezone.now()
    b.save()

    playerMatches= []
    inc=0
    allMatches=getMatches(player)
    while inc<(len(allMatches)):
        tes = getMatch(allMatches,inc)
        
        woww = Traits()
        listofpl = ((tes.get('metadata').get('participants')))
        plnames = []
        
        for puuid in listofpl:
            plnames.append(nameByPUUID(puuid))
        names= ','.join(plnames)
        
        playerpuuid=(player.get('puuid'))
        lamo = ((tes.get('info')).get('participants'))

        inc2 = 0
        for eachpl in lamo:
            if (playerpuuid==(eachpl.get('puuid'))):
                break
            inc2+=1

        swag = Matches()
        swag.otherParticipants = names
        swag.placement = (lamo[inc2]).get('placement')
        swag.game_length = (lamo[inc2]).get('time_eliminated')
        swag.game_time = timezone.now()
        swag.searchedPlayer = b
        swag.save()

        
        inc+=1


