from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect
from . import rebestplayer
from topplayers.reloadmatches import deleveryweek
from .loadaggdata import loadaggdata
import threading


def index(request):
    if request.method == 'POST':
        summoner_name = request.POST['inp_number']
        #players:player refers to topplayers/urls.py where app_name=players
        return redirect('players:player',player=summoner_name)
    
    removedb=threading.Thread(target=deleveryweek)
    removedb.start()
    
    return render(request, 'index.html')

def topplayers(request):
    if request.method == 'POST':
        if request.POST.get("Refresh"):
            is_running = threading.Event()
            result_container = []

            def threaded_operation():
                result = rebestplayer.cron_reloadbest()
                result_container.append(result)
                is_running.clear()  # Set the flag to indicate that the operation has completed

            # Create a new thread and assign the threaded_operation function as the target
            t = threading.Thread(target=threaded_operation, daemon=True)
            t.start()
            t.join()
    if rebestplayer.getPlayers().objects.count()>0:
        refreshed=rebestplayer.getPlayers().objects.first().add_date
    else: 
        return render(request, 'bestplayers.html')

    BestPlayers = list(rebestplayer.getPlayers().objects.values_list('autoinc', 'name', 'LP'))
    representedlist = []
    for player in BestPlayers:
        newplayer = (player[0]+1,player[1],player[2])
        representedlist.append(newplayer)

    players = {'toplayers':representedlist, 'refreshedtime':refreshed}
    return render(request, 'bestplayers.html', players)

# Create your views here.
