from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import rebestplayer, tes


def index(request):
    if request.method == 'POST':
        summoner_name = request.POST['inp_number']
        #players:player refers to topplayers/urls.py where app_name=players
        return redirect('players:player',player=summoner_name)
    return render(request, 'index.html')

def topplayers(request):
    print('hi')
    if request.method == 'POST':
        if request.POST.get("Refresh"):
            rebestplayer.cron_reloadbest()
    playerlist = tes.swa()
    print('klwdnglk')
    return HttpResponse(playerlist)
    #return render(request, 'bestplayers.html')




# Create your views here.
