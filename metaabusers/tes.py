from . import rebestplayer


def calculateBestPlayers():
    BestPlayers = list(rebestplayer.getPlayers().objects.values_list('autoinc', 'name', 'LP'))
    zipPlayers = list(zip(*BestPlayers))
    i=0
    swa=''
    while i<100000:
        swa=swa+str(i)
        i+=1
    # Perform further operations with zipPlayers if needed
    
    # Pass the result to the callback function
    return zipPlayers


