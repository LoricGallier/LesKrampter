# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 02:29:44 2019
File: emotion_webcam_demo.py
Author: Travis Tang (Voon Hao)
Github: https://github.com/travistangvh
Description: Real-time Emotion Classification Demo using Webcam
"""
from tensorflow.keras import models
import cv2
import numpy as np
from mtcnn.mtcnn import MTCNN
import sys
import os
from cursor import increase_cursor, decrease_cursor

def record_video() :
    #Importing the model
    trained_model = models.load_model('../trained_models/trained_vggface.h5', compile=False)
    trained_model.summary()

    # prevents openCL usage and unnecessary logging messages
    cv2.ocl.setUseOpenCL(False)
    # dictionary which assigns each label an emotion (alphabetical order)
    emotion_dict = {0: "Angry", 1: "Disgust", 2: "Fear", 3: "Happy", 4: "Sad", 5: "Surprise", 6: 'Neutral'}
    detector = MTCNN()
    # start the webcam feed
    cap = cv2.VideoCapture(0)
    black = np.zeros((96,96))

    angry = False
    angryTime = 0
    notAngryTime = 0
    angryIncreaseDelay = 3
    increaseAmount = 5

    while True:
        old_stdout = sys.stdout # backup current stdout
        sys.stdout = open(os.devnull, "w")
        # Find haar cascade to draw bounding box around face
        ret, frame = cap.read()
        if not ret:
            break
        # detect faces in the image
        results = detector.detect_faces(frame)
        # extract the bounding box from the first face
        sys.stdout = old_stdout # reset old stdout
        if len(results) == 1: #len(results)==1 if there is a face detected. len ==0 if no face is detected
            try:
                x1, y1, width, height = results[0]['box']
                x2, y2 = x1 + width, y1 + height
                # extract the face
                face = frame[y1:y2, x1:x2]
                #Draw a rectangle around the face
                cv2.rectangle(frame, (x1, y1), (x1+width, y1+height), (255, 0, 0), 2)
                # resize pixels to the model size
                cropped_img = cv2.resize(face, (96,96)) 
                cropped_img_expanded = np.expand_dims(cropped_img, axis=0)
                cropped_img_float = cropped_img_expanded.astype(float)
                prediction = trained_model.predict(cropped_img_float)
                #print(prediction)
                maxindex = int(np.argmax(prediction))
                #cv2.putText(frame, emotion_dict[maxindex], (x1+20, y1-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                
                if maxindex==0 and not angry:
                    angry = True
                    angryTime = 0
                    increase_cursor(increaseAmount)
                elif maxindex!=0 and angry:
                    angry = False
                    notAngryTime = 0
                    decrease_cursor(increaseAmount)
                else :
                    if angry:
                        angryTime += 1
                    else:
                        notAngryTime += 1
                    if(angryTime%angryIncreaseDelay==0 and angry):
                        increase_cursor(increaseAmount)
                    if(notAngryTime%angryIncreaseDelay==0 and not angry):
                        decrease_cursor(increaseAmount)
                
            except:
                pass
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
