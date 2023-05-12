from . import rebestplayer
import threading

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

def swa():
    is_running = threading.Event()

    # Define a container for the result
    result_container = []

    def threaded_operation():
        result = calculateBestPlayers()
        result_container.append(result)
        is_running.clear()  # Set the flag to indicate that the operation has completed

    # Create a new thread and assign the threaded_operation function as the target
    t = threading.Thread(target=threaded_operation)
    t.start()

    # Check if the threaded operation is still running
    while is_running.is_set():
        # The operation is running, perform actions accordingly
        print("Threaded operation is still in progress...")
        # You can perform additional actions while waiting for the operation to complete
        t.join(timeout=1)  # Wait for 1 second before checking the status again

    # Wait for the threaded operation to complete
    t.join()

    # Retrieve the result from the result container
    result = result_container[0] if result_container else None

    return result
