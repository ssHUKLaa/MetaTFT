from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from topplayers.withriotapi import getChallengerPlayers
from topplayers.models import Players

def index(request):
    if request.method == 'POST':
        summoner_name = request.POST['inp_number']
        #players:player refers to topplayers/urls.py where app_name=players
        return redirect('players:player',player=summoner_name)
    return render(request, 'index.html')

def topplayers(request):
    x=0
    hold=getChallengerPlayers()
    b= Players()
    try:
        while x<150:
            b.name=str(list(dict(list(hold.values())[x]).values())).strip("[]'")
            b.playerId=str(list(dict(list(hold.values())[x]).keys())).strip("[]'")
            b.LP=list(hold.keys())[x]
            x+=1
            b.save()
    except:
        return HttpResponse("na")
    return HttpResponse(str(getChallengerPlayers()))

# Create your views here.
