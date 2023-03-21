from riotwatcher import TftWatcher, ApiError

watcher= TftWatcher('RGAPI-36d0a802-4e5e-4f81-86a4-00641d9f24a2')



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
print(len(list((getChallengerPlayers().keys()))))

    