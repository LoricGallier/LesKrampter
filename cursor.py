import threading
from time import sleep
from output import update_luminosity, notify, get_volume

initialVolume = get_volume()

cursor_lock = threading.Lock()
cursor = 50

NEUTRAL, HAPPY, SAD, ANGRY, VERY_HAPPY = range(5)

def state():
    if is_neutral():
        return NEUTRAL
    elif is_happy():        
        return HAPPY
    elif is_sad():
        return SAD
    elif is_angry():
        return ANGRY
    elif is_very_happy():
        return VERY_HAPPY
    else:
        return NEUTRAL
    
    
def is_neutral():
    with cursor_lock:
        if cursor > 40 and cursor < 60:
            return True
        else :
            return False
    
def is_happy():
    with cursor_lock:
        if cursor > 60 and cursor < 80:
            return True
        else :
            return False
    
def is_sad():
    with cursor_lock:
        if cursor > 20 and cursor < 40:
            return True
        else :
            return False
    
def is_angry():
    with cursor_lock:
        if cursor > 0 and cursor < 20:
            return True
        else :
            return False
    
def is_very_happy():
    with cursor_lock:
        if cursor > 80 and cursor < 100:
            return True
        else :
            return False

def get_cursor():
    with cursor_lock:
        return cursor

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
        cursor = 50
    
def print_cursor():
    while True:
        with cursor_lock:
            print(cursor)
            update_luminosity(cursor)
            if cursor < 50:
                notify("L'écran pété", "Vous êtes en colère")
        sleep(5)
    

