from riotwatcher import TftWatcher, LolWatcher
from decouple import config
import requests, time
import ujson, datetime, pytz, re
apikey=config('apikey', cast=str)
watcher= TftWatcher(apikey,30)
lolwatcher= LolWatcher(apikey)
my_region = 'na1'
version=lolwatcher.data_dragon.versions_for_region(my_region)

def getChallengerPlayers():
    
    tes = watcher.league.challenger(my_region)
    entries = tes.get('entries')
    summonerRank = {}
    holder=0
    while holder < (len(entries)):
        # lp : ( summonerID : name)
        summonerRank.update({list(entries[holder].values())[2] : ({list(entries[holder].values())[0] : list(entries[holder].values())[1]})}) 
        holder+=1
    return ((dict(reversed(sorted(summonerRank.items())))))

def getGrandMasterPlayers():
    
    tes = watcher.league.grandmaster(my_region)
    entries = tes.get('entries')
    summonerRank = {}
    holder=0
    while holder < (len(entries)):
        # lp : ( summonerID : name)
        summonerRank.update({list(entries[holder].values())[2] : ({list(entries[holder].values())[0] : list(entries[holder].values())[1]})}) 
        holder+=1
    return ((dict(reversed(sorted(summonerRank.items())))))

def getMasterPlayers():
    
    tes = watcher.league.master(my_region)
    entries = tes.get('entries')
    summonerRank = {}
    holder=0
    while holder < (len(entries)):
        # lp : ( summonerID : name)
        summonerRank.update({list(entries[holder].values())[2] : ({list(entries[holder].values())[0] : list(entries[holder].values())[1]})}) 
        holder+=1
    return ((dict(reversed(sorted(summonerRank.items())))))

def getPlayer(summonerName):
    try:
        player= watcher.summoner.by_name(my_region, summonerName)
    except:
        return False
    else:
        return player

def playerByPUUID(puuid):
    try:
        player= watcher.summoner.by_puuid(my_region, puuid)
    except:
        return False
    else:
        return player
    
def searchPlayerStuff(id):
    try:
        player= watcher.league.by_summoner(my_region,id)[0]
    except:
        return False
    else:
        return player
    
def nameByPUUID(puuid):
    try:
        name = (watcher.summoner.by_puuid(my_region,puuid)).get('name')
    except:
        return False
    else:
        return name
    
def getProfilePicture(player):
    iconVerNum=str(version.get('n').get('profileicon'))
    profIconNum=str(dict(player).get('profileIconId'))
    imgFileName=(((((lolwatcher.data_dragon.profile_icons(iconVerNum)).get('data')).get(profIconNum))).get('image')).get('full')
    return (f'https://ddragon.leagueoflegends.com/cdn/{iconVerNum}/img/profileicon/{imgFileName}')

def rankIcon(rank):
    tiername=((rank.split())[0]).lower()
    return (f'https://raw.communitydragon.org/latest/plugins/rcp-fe-lol-shared-components/global/default/{tiername}.png')

def getMatches(player):
    
    matches=watcher.match.by_puuid(my_region,player.get('puuid'),10)
    
    return matches

def getMatch(matches, index):
    match=watcher.match.by_id(my_region,matches[index])
    
    return match 

def matchParticipants(match):
    participants = match.get('metadata').get('participants')
    return participants

def matchTime(match):
    return match.get('game_length')

def matchVersion(match):
    return match.get('game_version')

def loadstuff():
    
    getstuff = (requests.get('https://raw.communitydragon.org/latest/cdragon/tft/en_us.json')).text
    setdict = ujson.loads(getstuff)
    
    return setdict
    
def getCost(name, setnumber, setdict):
    for sets in (setdict.get('setData')):
        if (setnumber==sets.get('number')):
             for stuff in (sets.get('champions')):
                if (name==stuff.get('apiName')):
                    return stuff.get('cost')
                
def getTraitIconURL(name,setnumber, setdict):
    hold = ((setdict.get('sets')).get(str(setnumber)))
    for trait in hold.get('traits'):
        if (name==(trait.get('apiName'))):
            nameformat=(((trait.get('icon'))[(trait.get('icon')).rindex('/'):])[:-4]).lower()
            return f'https://raw.communitydragon.org/latest/game/assets/ux/traiticons{nameformat}.png'
        
def getItemIconURL(name, setdict):
    start=time.time()
    if name=="":
        return ""
    for stuff in (setdict.get('items')):
        if (stuff.get('apiName')==name):
            url=stuff.get('icon').lower()[:-4]
            print(time.time()-start)
            return f'https://raw.communitydragon.org/latest/game/{url}.png'
        
def getAugmentIconURL(name, setdict):
    if name=="":
        return ""
    for stuff in (setdict.get('items')):
        if (stuff.get('apiName')==name):
            url=stuff.get('icon').lower()[:-4]
            return f'https://raw.communitydragon.org/latest/game/{url}.png'

def getChampIconURL(name, setnumber, setdict):
    for sets in (setdict.get('setData')):
        if (setnumber==sets.get('number')):
             for stuff in (sets.get('champions')):
                if (name==stuff.get('apiName')):
                    nameformat=stuff.get('icon').lower()[:-4]
                    return f'https://raw.communitydragon.org/latest/game/{nameformat}.png'

#print(searchPlayerStuff((getPlayer('prestivent').get('id'))))
#swa=(((getMatch(getMatches(getPlayer('prestivent')),0)).get('metadata')))
#print(swa)
#print((getPlayer('prestivent')).get('id'))
#print(getPlayer('prestivent'))
#print(getMatches(getPlayer('Destroyernv')))
#print(((((setdict.get('setData'))[2]).get('champions'))[0]).keys())
#print(timezone.now()-(timezone.datetime.fromtimestamp((1685408445226/1000), tz=(timezone.get_current_timezone()))))
#print(timezone.now()-(timezone.datetime.strptime((timezone.datetime.fromtimestamp(1685758149029)), '%Y-%m-%d %H:%M:%S')))

#print(sorted(tes, key=lambda d: d['gametime']))

#swa=(datetime.datetime.strptime('1970'+' '+'5:06:54', "%Y%H:%M:%S"))

#print(datetime.datetime.now(tz=pytz.UTC))
#print(list(getChallengerPlayers().values()))
