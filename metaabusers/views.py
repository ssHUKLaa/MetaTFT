from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import rebestplayer, tes
import threading


def index(request):
    if request.method == 'POST':
        summoner_name = request.POST['inp_number']
        #players:player refers to topplayers/urls.py where app_name=players
        return redirect('players:player',player=summoner_name)
    return render(request, 'index.html')

def topplayers(request):
    if request.method == 'POST':
        if request.POST.get("Refresh"):
            result_container = []

            def threaded_operation():
                result = rebestplayer.cron_reloadbest()
                result_container.append(result)
                is_running.clear()  # Set the flag to indicate that the operation has completed

            # Create a new thread and assign the threaded_operation function as the target
            t = threading.Thread(target=threaded_operation, daemon=True)
            t.start()
            # Check if the threaded operation is still running
    is_running = threading.Event()

    # Define a container for the result
    result_container = []

    def threaded_operation():
        result = tes.calculateBestPlayers()
        result_container.append(result)
        is_running.clear()  # Set the flag to indicate that the operation has completed

    # Create a new thread and assign the threaded_operation function as the target
    t = threading.Thread(target=threaded_operation, daemon=True)
    t.start()

    # Check if the threaded operation is still running

    # Wait for the threaded operation to complete
    t.join()

    # Retrieve the result from the result container
    result = result_container[0] if result_container else None
    print(result)

    return render(request, 'bestplayers.html')




# Create your views here.
