import subprocess
import threading
from cursor import print_cursor
from get_text import record_text
from output import get_display_name, set_luminosity, set_volume
from video.src.emotion_webcam_demo import record_video
from transformers import logging


logging.set_verbosity_error()

thread_text = threading.Thread(target = record_text)  
thread_video = threading.Thread(target = record_video)
thread_cursor = threading.Thread(target = print_cursor)

thread_text.start()
thread_video.start()
thread_cursor.start()

thread_text.join()  
thread_video.join()
thread_cursor.join()

subprocess.call(['xrandr', '--output', get_display_name(), '--brightness', str(float(1))])