import threading
import cursor
import text_emotion
from get_text import record_text
from cursor import print_cursor


def main():
    thread_text = threading.Thread(target = record_text)  
    #thread_video = threading.Thread(target = record_video)
    thread_cursor = threading.Thread(target = print_cursor)
    
    thread_text.start()
    #thread_video.start()
    thread_cursor.start()
    
    
    thread_text.join()  
    #thread_video.join()
    thread_cursor.join()


main()