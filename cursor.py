import threading
from time import sleep
from output import update_luminosity, notify, get_volume, update_volume

initialVolume = get_volume()

cursor_lock = threading.Lock()
cursor = 100

def increase_cursor(value):
    with cursor_lock:
        global cursor
        cursor += value
        if cursor > 100:
            cursor = 100

def decrease_cursor(value):
    with cursor_lock:
        global cursor
        cursor -= value
        if cursor < 0:
            cursor = 0
        

def reset_cursor():
    with cursor_lock:
        global cursor
        cursor = 100
    
def print_cursor():
    notif_count = 0
    initial_volume = get_volume()
    while True:
        print(cursor)
        update_luminosity(cursor)
        update_volume(cursor, initial_volume)
        if cursor < 40 & notif_count == 0:
            notif_count = 5
            notify("Fort stress détecté", "Vous devriez prendre une pause")
        elif cursor < 60 & notif_count == 0:
            notif_count = 5
            notify("Énervement détecté", "Luminosité réduite")
        elif notif_count != 0:
            notif_count -= 1
        sleep(5)
    

