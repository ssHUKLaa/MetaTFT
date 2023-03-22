from django.shortcuts import render
from django.http import HttpResponse
from .withriotapi import getChallengerPlayers
from .models import Players

def index(request):
    x=0
    hold=getChallengerPlayers()
    b= Players()
    while x<150:
        b.name=str(list(dict(list(hold.values())[x]).values())).strip("[]'")
        b.playerId=str(list(dict(list(hold.values())[x]).keys())).strip("[]'")
        b.LP=list(hold.keys())[x]
        x+=1
        b.save()
    
    return HttpResponse(str(getChallengerPlayers()))
# Create your views here.
