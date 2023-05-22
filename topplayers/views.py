from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .withriotapi import getPlayer, getProfilePicture
from .reloadmatches import fillDb
import threading

def index(request):
    return HttpResponse("N/A")

def players_by_api(request, player):
    if request.method == 'POST':
        summoner_name = request.POST['inp_number']
        #players:player refers to topplayers/urls.py where app_name=players
        return redirect('players:player',player=summoner_name)
    contestant=(getPlayer(player))
    if (contestant==False):
        return HttpResponse(f'not a person')
    profpic=(getProfilePicture(contestant))
    fillDb(contestant)
    
    playername={"player": contestant.get('name'), "profpic": profpic}
    return render(request, 'topplayers/player.html',playername)
# Create your views here.
