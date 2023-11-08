from plyer import notification
import subprocess
import time

current_luminosity = 100
limits = [20, 40, 60, 80]
updating_luminosity = False

def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_name = "L'écran pété",
        timeout = 100,
    )

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

def update_luminosity(emotionRate): # 0: Très en colère, 100: normal
    global updating_luminosity
    if not updating_luminosity:
        updating_luminosity = True
        new_level = 100
        for i in range(0, len(limits)):
            if emotionRate < limits[i]:
                new_level = int(limits[i] / 100 * current_luminosity)
                break
        set_luminosity(get_display_name(), new_level)
        updating_luminosity = False