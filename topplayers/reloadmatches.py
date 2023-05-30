from .models import Matches, searchPlayers, Champions, Traits
from django.utils import timezone
from .withriotapi import searchPlayerStuff, getMatches, getMatch, nameByPUUID

def fillDb(player,matches):

    count=(((searchPlayers.objects.filter(name=player.get('playername'))).count()))
    '''
    if count>0:
        ss=(searchPlayers.objects.filter(name=player.get('playername')))
        time=(ss.values()[0].get('add_date'))
        nowtime=timezone.now()
        diff=((nowtime-time))
        print(diff.seconds//3600)
        if ((((diff.seconds//3600))<5)):
            return None
    '''
        
    b=searchPlayers()
    b.name=(player.get('playername'))
    b.id=(player.get('id'))
    b.tier=player.get('tier')
    b.LP=player.get('LP')
    b.add_date=player.get('dateadded')
    b.save()

    for eachmatch in matches:

        swag = Matches()
        swag.id=eachmatch.get('id')
        swag.otherParticipants = eachmatch.get('otherparticipants')
        swag.placement = eachmatch.get('placement')
        swag.game_length = eachmatch.get('game_length')
        swag.game_time = eachmatch.get('game_time')
        swag.searchedPlayer = b
        swag.save()

        traitlist=eachmatch.get('traits')
        inctrait=0
        for trait in traitlist:
            weow = Traits()
            weow.id = eachmatch.get('id')+(','+str(inctrait))
            weow.traitname = trait.get('name')
            weow.currenttier = trait.get('tier')
            weow.tierunits = trait.get('numUnits')
            weow.associatedMatch = swag
            weow.save()
            inctrait+=1
        
        unitlist = eachmatch.get('champions')
        incchamps=0
        for unit in unitlist:
            loll = Champions()
            loll.id = eachmatch.get('id')+(','+str(incchamps))
            loll.Name = unit.get('name')
            loll.Star = unit.get('Star')
            loll.Items = ','.join(unit.get('Items'))
            loll.Rarity = unit.get('Rarity')
            loll.associatedMatch = swag
            loll.save()
            incchamps+=1

def deleveryweek():
    for swag in searchPlayers.objects.all():
        timeadded=swag.add_date
        if (((timezone.now()-timeadded).days)>=7):
            swag.delete()
        
def playerStats(player):
    x = searchPlayerStuff(player.get('id'))
    if (x==False):
        dictofstats={'playername':player.get('name'), 'tier':'N/A', 'LP':-1,'dateadded':timezone.now(), 'id':player.get('id')}
        return dictofstats
    dictofstats={'playername':player.get('name'), 'tier':(x.get('tier'))+" "+x.get('rank'), 'LP':x.get('leaguePoints'),'dateadded':timezone.now(), 'id':player.get('id')}
    return dictofstats

def matchesfordisp(player):
    allMatches=getMatches(player)
    inc=0
    matchlist=[]
    while inc<(len(allMatches)):
        tes = getMatch(allMatches,inc)

        listofpl = ((tes.get('metadata').get('participants')))
        plnames = []
        
        for puuid in listofpl:
            plnames.append(nameByPUUID(puuid))
        
        playerpuuid=(player.get('puuid'))
        lamo = ((tes.get('info')).get('participants'))

        inc2 = 0
        for eachpl in lamo:
            if (playerpuuid==(eachpl.get('puuid'))):
                break
            inc2+=1

        traitlist=lamo[inc2].get('traits')
        traits=[]
        for trait in traitlist:
            traitdict={'name':trait.get('name'),'tier':trait.get('tier_current'),'numUnits':trait.get('num_units')}
            traits.append(traitdict)
        
        unitlist = lamo[inc2].get('units')
        champs=[]
        for unit in unitlist:
            champdict={'name':unit.get('character_id'),'Star':unit.get('tier'),'Items':unit.get('itemNames'),'Rarity':unit.get('rarity')}
            champs.append(champdict)

        matchdict={'id':allMatches[inc],
                   'otherparticipants':plnames,
                   'placement':(lamo[inc2]).get('placement'),
                   'game_time':timezone.now(),
                   'game_length':(lamo[inc2]).get('time_eliminated'), 
                   'traits':traits,
                   'champions':champs
                   }
        matchlist.append(matchdict)
        inc+=1
    return matchlist
    