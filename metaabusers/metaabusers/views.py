from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from topplayers.withriotapi import getChallengerPlayers
from . import rebestplayer
from django.core.management import call_command

def index(request):
    if request.method == 'POST':
        summoner_name = request.POST['inp_number']
        #players:player refers to topplayers/urls.py where app_name=players
        return redirect('players:player',player=summoner_name)
    call_command('crontab add')
    return render(request, 'index.html')

def topplayers(request):
    rebestplayer.cron_reloadbest()
    return HttpResponse(str(getChallengerPlayers()))

# Create your views here.
