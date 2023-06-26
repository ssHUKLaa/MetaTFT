from .models import Matches, searchPlayers, Champions, Traits
from django.utils import timezone
from .withriotapi import searchPlayerStuff, getMatches, getMatch, nameByPUUID, loadstuff, getCost, getTraitIconURL, getItemIconURL, getAugmentIconURL, getChampIconURL
from concurrent.futures import ThreadPoolExecutor
import time, re

def fillDb(player,matches):
    
    count=(((searchPlayers.objects.filter(name=player.get('playername'))).count()))
    '''
    if count>0:
        ss=(searchPlayers.objects.filter(name=player.get('playername')))
        time=(ss.values()[0].get('add_date'))
        nowtime=timezone.now()
        diff=((nowtime-time))
        if ((diff.days)>=1):
            diff=(diff.days)*86400
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

    lmfaaoo = (Matches.objects.filter(searchedPlayer=b.id))
    if ((lmfaaoo.count())>0):
        for plmatches in lmfaaoo:
            gametime_str = plmatches.game_time
            parts = gametime_str.split(', ')
            if len(parts) == 2:  # Check if the string representation includes days
                days = int(parts[0].split()[0])  # Extract the number of days
                time = parts[1]
            else:
                days = 0
                time = parts[0]

            time_parts = [int(part) for part in time.split(':')]
            total_time = timezone.timedelta(days=days, hours=time_parts[0], minutes=time_parts[1], seconds=time_parts[2])

            if total_time > timezone.timedelta(days=5):
                plmatches.delete()

    for eachmatch in matches:

        swag = Matches()
        swag.id=eachmatch.get('id')
        swag.otherParticipants = ','.join(eachmatch.get('otherparticipants'))
        swag.placement = eachmatch.get('placement')
        swag.game_length = eachmatch.get('game_length')
        swag.game_time = eachmatch.get('game_time')
        swag.set_number = eachmatch.get('set_number')
        swag.augments = ','.join(eachmatch.get('augments'))
        swag.augments_icon = ','.join(eachmatch.get('augments_icon'))
        swag.searchedPlayer = b
        swag.save()

        traitlist=eachmatch.get('traits')
        inctrait=0
        for trait in traitlist:
            weow = Traits()
            weow.id = eachmatch.get('id')+(','+str(inctrait))
            weow.traitname = trait.get('Name')
            weow.currenttier = trait.get('tier')
            weow.style = trait.get('style')
            weow.imageIcon = trait.get('imageIcon')
            weow.associatedMatch = swag
            weow.save()
            inctrait+=1
        
        unitlist = eachmatch.get('champions')
        incchamps=0
        for unit in unitlist:
            loll = Champions()
            loll.id = eachmatch.get('id')+(','+str(incchamps))
            loll.Name = unit.get('Name')
            loll.Champ_icon = unit.get('Champ_icon')
            loll.Star = unit.get('Star')
            loll.Items = ','.join(unit.get('Items'))
            loll.Item_icon = ','.join(unit.get('Item_icon'))
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
    matchlist=[]
    stuff=loadstuff()

    def process_match(inc):
        tes = getMatch(allMatches,inc)

        listofpl = ((tes.get('metadata').get('participants')))
        plnames = [nameByPUUID(puuid) for puuid in listofpl]
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
            traitdict={'Name':(trait.get('name'))[5:].lower(),'tier':trait.get('tier_current'),'style':trait.get('style'),'imageIcon':getTraitIconURL(trait.get('name'),(tes.get('info').get('tft_set_number')),stuff)}
            traits.append(traitdict)
        
        unitlist = lamo[inc2].get('units')
        champs=[]

        for unit in unitlist:
            Name=(unit.get('character_id'))
            champdict={'Name':Name.lower(),
                       'Champ_icon':getChampIconURL(Name,(tes.get('info').get('tft_set_number')),stuff),
                       'Star':unit.get('tier'),
                       'Items':unit.get('itemNames'),
                       'Item_icon':[getItemIconURL(name, stuff) for name in (unit.get('itemNames'))],
                       'Rarity':getCost(unit.get('character_id'),(tes.get('info').get('tft_set_number')), stuff)}
            champs.append(champdict)

        matchdict={'id':allMatches[inc],
                   'otherparticipants':plnames,
                   'placement':(lamo[inc2]).get('placement'),
                   'game_time':((str(timezone.now()-(timezone.datetime.fromtimestamp((((tes.get('info')).get('game_datetime'))/1000), tz=(timezone.get_current_timezone()))))).split('.'))[0],
                   'game_length':time.strftime("%M:%S",time.gmtime(float(((lamo[inc2]).get('time_eliminated'))))), 
                   'set_number': (tes.get('info').get('tft_set_number')),
                   'augments':(lamo[inc2]).get('augments'),
                   'augments_icon':[getAugmentIconURL(name, stuff) for name in (lamo[inc2]).get('augments')], 
                   'traits':traits,
                   'champions':champs
                   }
        return matchdict
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(process_match, inc) for inc in range(len(allMatches))]
        for future in futures:
            match = future.result()
            if match:
                matchlist.append(match)
    
    return matchlist

def timedelta_str_to_posix(time_str):
    if "day" in time_str:
        days, time = time_str.split(", ")
        days = int(days.split()[0])
    else:
        days = 0
        time = time_str
    hours, minutes, seconds = map(int, time.split(":"))
    timedelta_obj = timezone.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    posix_timestamp = (timezone.now()).timestamp() + timedelta_obj.total_seconds()
    return posix_timestamp

def gametimefromDB(timedelta, dbdatetime):
    initial_datetime = dbdatetime

    # Time delta
    time_delta_str = timedelta

    # Parse time delta components
    days, hours, minutes, seconds = 0, 0, 0, 0
    pattern1 = r"(\d+):(\d+):(\d+)"
    pattern2 = r"(\d+)\s*day[s]*,\s*(\d+):(\d+):(\d+)"
    match1 = re.match(pattern1, time_delta_str)
    match2 = re.match(pattern2, time_delta_str)
    if match1:
        hours, minutes, seconds = map(int, match1.groups())
    elif match2:
        days, hours, minutes, seconds = map(int, match2.groups())

    # Create timedelta object
    time_delta = timezone.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

    # Subtract timedelta from datetime
    result_datetime = initial_datetime - time_delta
    timedeltanow = timezone.now()-result_datetime
    
    hours, remainder = divmod(timedeltanow.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if timedeltanow.days == 0:
        time_delta_str = f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        time_delta_str = f"{timedeltanow.days} day, {hours:02}:{minutes:02}:{seconds:02}"

    return (time_delta_str)

def testart():
    return time.time()

def tesend(start):
    print(time.time()-start)