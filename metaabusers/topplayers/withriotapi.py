from riotwatcher import TftWatcher, ApiError, LolWatcher
from datetime import datetime
from django.utils import timezone
apikey='RGAPI-fc9d4dd6-fe7a-45a7-a413-250d8779fdfd'
watcher= TftWatcher(apikey)
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

def getPlayer(summonerName):
    try:
        player= watcher.summoner.by_name(my_region, summonerName)
    except:
        return False
    else:
        return player
    
def getProfilePicture(player):
    iconVerNum=str(version.get('n').get('profileicon'))
    profIconNum=str(dict(player).get('profileIconId'))
    imgFileName=(((((lolwatcher.data_dragon.profile_icons(iconVerNum)).get('data')).get(profIconNum))).get('image')).get('full')
    return (f'https://ddragon.leagueoflegends.com/cdn/{iconVerNum}/img/profileicon/{imgFileName}')

def getMatches(player):
    matches=watcher.match.by_puuid(my_region,player.get('puuid'))

    match=watcher.match.by_id(my_region,matches[0])
    return str((((match.get('info')).get('participants')))[5])
    matchinfo=match.get('info')

def matchTime(match):
    return match.get('game_length')

def matchVersion(match):
    return match.get('game_version')


