from riotwatcher import TftWatcher, ApiError
from datetime import datetime
from django.utils import timezone
watcher= TftWatcher('RGAPI-c39b5926-1ef1-4c6e-b383-76cdc87d20e2')
my_region = 'na1'
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
        return player.values()
    matches=watcher.match.by_puuid(my_region,player.get('puuid'))
    match=watcher.match.by_id(my_region,matches[0])
    matchinfo=match.get('info')

