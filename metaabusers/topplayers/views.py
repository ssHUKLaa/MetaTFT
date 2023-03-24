from django.shortcuts import render
from django.http import HttpResponse
from .withriotapi import getChallengerPlayers, getPlayer
from .models import Players

def index(request):
    return HttpResponse("N/A")

def players_by_api(request, player):
    if (getPlayer(player)==False):
        return HttpResponse(f'not a person')
    return HttpResponse(getPlayer(player))
# Create your views here.
