import threading
from get_text import record_text
from cursor import print_cursor
from video.src.emotion_webcam_demo import record_video
from transformers import logging


def main():
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


main()