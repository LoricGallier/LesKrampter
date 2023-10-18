import threading
from get_text import record_text
from video.src.emotion_webcam_demo import record_video


def main():
    thread_text = threading.Thread(target = record_text)  
    thread_video = threading.Thread(target = record_video)
    
    thread_text.start()
    thread_video.start()
    
    
    thread_video.join()
    thread_text.join()  
