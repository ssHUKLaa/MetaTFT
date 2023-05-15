from . import rebestplayer


def calculateBestPlayers():
    BestPlayers = list(rebestplayer.getPlayers().objects.values_list('autoinc', 'name', 'LP'))
    zipPlayers = list(zip(*BestPlayers))
    i=0
    swa=''
    # Perform further operations with zipPlayers if needed
    
    # Pass the result to the callback function
    return zipPlayers


