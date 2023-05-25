from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .withriotapi import getPlayer, getProfilePicture
from .reloadmatches import fillDb, playerStats, matchesfordisp
from .models import searchPlayers, Matches, Champions, Traits
import threading

def index(request):
    return HttpResponse("N/A")

def players_by_api(request, player):
    playermatches= []
    contestant=(getPlayer(player))
    playerstats=None
    initdispmatches=None
    if request.method == 'POST':
        if 'Refresh' in request.POST:
            playerstats=playerStats(contestant)
            initdispmatches= matchesfordisp(contestant)
            filldbsep=threading.Thread(target=fillDb(contestant))
            filldbsep.start()

        elif 'searchPl' in request.POST:
            summoner_name = request.POST['inp_number']
            #players:player refers to topplayers/urls.py where app_name=players
            return redirect('players:player',player=summoner_name)
    
    if (contestant==False):
        return HttpResponse(f'not a person')
    profpic=(getProfilePicture(contestant))
    count=(((searchPlayers.objects.filter(name=contestant.get('name'))).count()))

    statsdict=None
    if ((count>0) and (playerstats==None)):
        playerbyid=(searchPlayers.objects.filter(id=contestant.get('id')).first())
        statsdict={'tier':playerbyid.tier,'LP':playerbyid.LP,'dateadded':playerbyid.add_date}

        matches=Matches.objects.filter(searchedPlayer=contestant.get('id'))
        for match in matches:
            particpants=((match.otherParticipants).split(','))
            champlist=[]
            traitlist=[]
            for champion in Champions.objects.filter(associatedMatch=match.id):
                Items=((champion.Items).split(','))
                champinfo={'dispindex':(champion.id)[len(champion.id)-1],'Items':Items,'Name':champion.Name,'Star':champion.Star, 'Rarity':champion.Rarity+1}
                champlist.append(champinfo)
            for trait in Traits.objects.filter(associatedMatch=match.id):
                traitinfo={'dispindex':(trait.id)[len(champion)-1],'Name':trait.Name, 'numUnits':trait.tierunits}
                traitlist.append(traitinfo)

            matchdict= {'placement':match.placement, 'participants':particpants,'timeofgame':match.game_time,'lengthofgame':match.game_length, 'Champions':champlist, 'Traits':traitlist}

            playermatches.append(matchdict)
            
    statsdisp=playerstats
    matchesdisp=initdispmatches
    if (playerstats==None):
        statsdisp=statsdict
        matchesdisp=playermatches
    
    playername={"player": contestant.get('name'), "profpic": profpic, "stats":statsdisp,"matches":matchesdisp}
    return render(request, 'topplayers/player.html',playername)
# Create your views here.
