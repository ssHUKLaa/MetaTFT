from .models import Matches, searchPlayers
from django.utils import timezone
from .withriotapi import searchPlayerStuff, getMatches, getMatch

def fillDb(player):
    time=timezone.now()
    playerMatches= []
    inc=0
    allMatches=getMatches(player)
    while inc<(len(allMatches)):
        playerMatches.append(getMatch(allMatches,inc))
        inc+=1
    
    x = searchPlayerStuff(player.get('id'))
    pl=searchPlayers
        
    
    

