from metaabusers.models import AggregateData
from random import choice
import statistics

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

def compareMatchToAgg(aggdata, champs, augments):
    percentsimilar=[]
    for champion in champs:
        for aggmatch in aggdata:
            matchsimilar=[]
            for aggunit in aggmatch:
                unitsimilar=0
                if (champion.get('Name')==aggunit.get('Name')):
                    unitsimilar+=0.85
                    for aggunititem in ((aggunit.get('Items')).split(',')):
                        for champitem in champion.get('Items'):
                            if (champitem==aggunititem):
                                unitsimilar+=0.05
                else:
                    for aggunititem in ((aggunit.get('Items')).split(',')):
                        for champitem in champion.get('Items'):
                            if (champitem==aggunititem):
                                unitsimilar+=0.10
                matchsimilar.append(unitsimilar)
            totalmatchsim=(statistics.mean(matchsimilar))
            if totalmatchsim<0.70:
                for aggmatchaugment in (((aggmatch[0]).get('Augments')).split(',')):
                    for matchaug in augments:
                        if matchaug==aggmatchaugment:
                            totalmatchsim+=0.05
            percentsimilar.append(totalmatchsim)
    return (statistics.mean(percentsimilar)*100)