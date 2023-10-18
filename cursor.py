
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
    if cursor > 40 and cursor < 60:
        return True
    else :
        return False
    
def is_happy():
    if cursor > 60 and cursor < 80:
        return True
    else :
        return False
    
def is_sad():
    if cursor > 20 and cursor < 40:
        return True
    else :
        return False
    
def is_angry():
    if cursor > 0 and cursor < 20:
        return True
    else :
        return False
    
def is_very_happy():
    if cursor > 80 and cursor < 100:
        return True
    else :
        return False

def get_cursor():
    return cursor

def increase_cursor(value):
    global cursor
    cursor += value
    if cursor > 100:
        cursor = 100
def decrease_cursor(value):
    global cursor
    cursor -= value
    if cursor < 0:
        cursor = 0

def reset_cursor():
    global cursor
    cursor = 50
    

    

