from riotwatcher import TftWatcher, ApiError

watcher= TftWatcher('')



def getChallengerPlayers():
    my_region = 'na1'
    tes = watcher.league.challenger(my_region)
    entries = tes.get('entries')
    summonerRank = {}
    IDRankSummoner = {}
    holder=0;
    while holder < len(entries):
        summonerRank.update({list(entries[holder].values())[1] : list(entries[holder].values())[2]})
        IDRankSummoner.update({list(entries[holder].values())[0] : summonerRank})
        holder+=1
    return (str(IDRankSummoner))


    