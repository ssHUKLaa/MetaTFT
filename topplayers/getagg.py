from metaabusers.models import AggregateData
from random import choice

def loadAggData():
    x=0
    agglist=[]
    pks = AggregateData.objects.values_list('id', flat=True)
    new_pks=[id[:2] for id in pks]
    uniqueids=list(set(new_pks))
    while x<10:
        random_pk = choice(uniqueids)
        random_objs = AggregateData.objects.filter(id__contains = random_pk)
        agglist.append(list(random_objs))
        x+=1
    return agglist

def compareMatchToAgg(aggdata, champs):
    percentsimilar=0
    for champion in champs:
        for aggmatch in aggdata:
                for aggunit in aggmatch:
                     if 