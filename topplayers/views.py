from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from .withriotapi import getPlayer, getProfilePicture, rankIcon
from .reloadmatches import fillDb, playerStats, matchesfordisp, timedelta_str_to_posix, gametimefromDB
from .models import searchPlayers, Matches, Champions, Traits
from operator import itemgetter
import time
import threading

def index(request):
    return HttpResponse("N/A")

def players_by_api(request, player):
    playermatches= []
    contestant=(getPlayer(player))
    playerstats=None
    initdispmatches=None
    refreshed = False
    if request.method == 'POST':
        if 'Refresh' in request.POST:
            playerstats=playerStats(contestant)
            initdispmatches= matchesfordisp(contestant)
            refreshed = True
            tes=threading.Thread(target=fillDb,args=(playerstats,initdispmatches))
            tes.start()
        elif 'searchPl' in request.POST:
            summoner_name = request.POST['inp_number']
            #players:player refers to topplayers/urls.py where app_name=players
            return redirect('players:player',player=summoner_name)
    
    if (contestant==False):
        return HttpResponse(f'not a person')
    profpic=(getProfilePicture(contestant))
    count=(((searchPlayers.objects.filter(name=contestant.get('name'))).count()))
    
    statsdict=None
    if ((count>0) and (refreshed==False)):
        playerbyid=(searchPlayers.objects.filter(id=contestant.get('id')).first())
        statsdict={'tier':playerbyid.tier,'LP':playerbyid.LP,'dateadded':playerbyid.add_date}

        matches=Matches.objects.filter(searchedPlayer=contestant.get('id'))
        theplayer=(searchPlayers.objects.filter(id=contestant.get('id')))[0]
        for match in matches:
            participants=((match.otherParticipants).split(','))
            champlist=[]
            traitlist=[]
            for champion in Champions.objects.filter(associatedMatch=match.id):
                Items=((champion.Items).split(','))
                champinfo={'dispindex':(champion.id)[len(champion.id)-1],
                           'Items':Items,
                           'Name':((champion.Name).lower()),
                           'Star':champion.Star, 
                           'Rarity':champion.Rarity
                           }
                champlist.append(champinfo)
            for trait in Traits.objects.filter(associatedMatch=match.id):
                traitinfo={'Name':trait.traitname,
                           'tier': trait.currenttier,
                           'style': trait.style,
                           'imageIcon':trait.imageIcon}
                traitlist.append(traitinfo)

            matchdict= {'placement':match.placement, 
                        'otherparticipants':participants,
                        'game_time':gametimefromDB(match.game_time, theplayer.add_date),
                        'game_length':match.game_length, 
                        'set_number':match.set_number,
                        'champions':champlist,
                        'traits':traitlist
                        }
            playermatches.append(matchdict)
        playermatches = sorted(playermatches,key=lambda x: timedelta_str_to_posix(x['game_time']))

        
    elif (playerstats==None):
        playerstats=playerStats(contestant)
            
    if (refreshed==True):
        statsdisp=playerstats
        matchesdisp=initdispmatches
    elif (refreshed==False and count>0):
        statsdisp=statsdict
        matchesdisp=playermatches
    elif (refreshed==False and count==0):
        statsdisp=playerstats
        matchesdisp=initdispmatches

        
    icon=(rankIcon('unranked I'))
    if (statsdisp.get('tier')!='N/A'):
        icon=(rankIcon(statsdisp.get('tier')))
    
    playername={"player": contestant.get('name'), "profpic": profpic,"stats":statsdisp,"matches":matchesdisp, "rankicon": icon}
    return render(request, 'topplayers/player.html',playername)
# Create your views here.
