from plyer import notification
import subprocess
import time

updating_luminosity = False
updating_volume = False
current_luminosity = 100

# Notifications
def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_name = "L'écran pété",
        timeout = 100,
    )

# Luminosité
def get_display_name():
    xrandr_output = subprocess.check_output(['xrandr']).decode('utf-8')

    for line in xrandr_output.splitlines():
        if ' connected' in line:
            display_name = line.split()[0]
            return display_name
        
def set_luminosity(display_name, level): # level goes from 0 to 100
    global current_luminosity
    if level < current_luminosity:
        for brightness_level in reversed(range(level-1, current_luminosity)):
            subprocess.call(['xrandr', '--output', display_name, '--brightness', str(float((brightness_level)/100))])
            time.sleep(0.1)
    else:
        for brightness_level in range(current_luminosity, level):
            subprocess.call(['xrandr', '--output', display_name, '--brightness', str(float(brightness_level/100))]) 
            time.sleep(0.1)
    current_luminosity = level

def update_luminosity(emotionRate): # 0: Très en colère, 100: calme
    global updating_luminosity
    if not updating_luminosity:
        updating_luminosity = True
        new_level = 100
        if emotionRate <= 40:
            new_level = 40
        elif emotionRate <= 60:
            new_level = 60
        elif emotionRate <= 80:
            new_level = 80
        set_luminosity(get_display_name(), new_level)
        updating_luminosity = False

# Volume
def set_volume(level):
    subprocess.check_output("amixer -D pulse sset Master " + str(level) + "%", shell=True, text=True)

def get_volume():
    volume = subprocess.check_output("amixer -D pulse get Master | awk -F '[][]' '/Front Left: Playback/ {print $2}'", shell=True, text=True)
    return int(volume[:-2])

# A partir du niveau de colère en entrée, le son évolue progressiment jusqu'à un certain pourcentage
# du volume initial (ces pourcentages sont définis dans la liste "limits")
def update_volume(emotion_level, initial_volume): # 0: Très en colère, 100: normal
    global updating_volume
    if not updating_volume:
        updating_volume = True
        new_volume = int(initial_volume*(emotion_level/100))
        set_volume(new_volume)
        updating_volume = False