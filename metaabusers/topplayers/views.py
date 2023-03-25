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
    contestant=getPlayer(player)
    tes=requests.get(getProfilePicture(contestant))
    return HttpResponse(tes.content, content_type="image/png")
# Create your views here.
