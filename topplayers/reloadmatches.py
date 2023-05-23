from .models import Matches, searchPlayers, Champions, Traits
from django.utils import timezone
from .withriotapi import searchPlayerStuff, getMatches, getMatch, nameByPUUID

def fillDb(player):
    x = searchPlayerStuff(player.get('id'))
    count=(((searchPlayers.objects.filter(name=player.get('name'))).count()))
    if count>0:
        ss=(searchPlayers.objects.filter(name=player.get('name')))
        time=(ss.values()[0].get('add_date'))
        nowtime=timezone.now()
        diff=((nowtime-time))
        print(diff.seconds//3600)
        if (((diff.seconds//3600))<5):
            return None
        
    if ((x==False)):
        b=searchPlayers()
        b.name=(player.get('name'))
        b.id=(player.get('id'))
        b.LP=-1
        b.add_date=timezone.now()
        b.save()
    b=searchPlayers()
    b.name=(player.get('name'))
    b.id=(player.get('id'))
    b.LP=x.get('leaguePoints')
    b.add_date=timezone.now()
    b.save()

    inc=0
    allMatches=getMatches(player)
    while inc<(len(allMatches)):
        tes = getMatch(allMatches,inc)
        
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
        swag.id=allMatches[inc]
        swag.otherParticipants = names
        swag.placement = (lamo[inc2]).get('placement')
        swag.game_length = (lamo[inc2]).get('time_eliminated')
        swag.game_time = timezone.now()
        swag.searchedPlayer = b
        swag.save()

        traitlist=lamo[inc2].get('traits')
        inctrait=0
        for trait in traitlist:
            weow = Traits()
            weow.id = allMatches[inc]+(','+str(inctrait))
            weow.traitname = trait.get('name')
            weow.currenttier = trait.get('tier_current')
            weow.tierunits = trait.get('num_units')
            weow.associatedMatch = swag
            weow.save()
            inctrait+=1
        
        unitlist = lamo[inc2].get('units')
        incchamps=0
        for unit in unitlist:
            loll = Champions()
            loll.id = allMatches[inc]+(','+str(incchamps))
            loll.Name = unit.get('character_id')
            loll.Star = unit.get('tier')
            loll.Items = ','.join(unit.get('itemNames'))
            loll.Rarity = unit.get('rarity')
            loll.associatedMatch = swag
            loll.save()
            incchamps+=1

        inc+=1
