from riotwatcher import TftWatcher, ApiError

watcher= TftWatcher('')

my_region = 'na1'
tes = watcher.league.challenger(my_region)

entries = tes.get('entries')
summonerRank = {}
print(summonerRank.keys())

print("lp"+str((list(entries[0].values()))[2])+"name"+(list(entries[0].values()))[1])

holder=0;
while holder < len(entries):
    summonerRank.update({list(entries[holder].values())[1] : list(entries[holder].values())[2]})
    holder+=1
print(summonerRank)

    