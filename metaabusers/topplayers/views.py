from django.shortcuts import render
from django.http import HttpResponse
from .withriotapi import getChallengerPlayers, getPlayer, getMatches, getProfilePicture
from .models import Players
import requests

def index(request):
    return HttpResponse("N/A")

def players_by_api(request, player):
    if (getPlayer(player)==False):
        return HttpResponse(f'not a person')
    contestant=(getPlayer(player))
    tes=(getProfilePicture(contestant))
    playername={"player": contestant.get('name'), "profpic": tes}
    profilepic={"profpic": tes}
    return render(request, 'topplayers/player.html',playername)
# Create your views here.
