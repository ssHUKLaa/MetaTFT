from riotwatcher import TftWatcher, ApiError
from .models import Players
watcher= TftWatcher('RGAPI-8cc2d203-6835-4a74-9713-6b08d96c02b8')



def getChallengerPlayers():
    my_region = 'na1'
    tes = watcher.league.challenger(my_region)
    entries = tes.get('entries')
    summonerRank = {}
    holder=0;
    while holder < (len(entries)):
        # lp : ( summonerID : name)
        summonerRank.update({list(entries[holder].values())[2] : ({list(entries[holder].values())[0] : list(entries[holder].values())[1]})}) 
        holder+=1
    return ((dict(reversed(sorted(summonerRank.items())))))
