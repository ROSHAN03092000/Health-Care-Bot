#Coded and presented by: Roshan Ravi Kumar Shetti
#From:RV Institute of technology and management
#Under the guidance of Yashwant sir
#From: Loginware

import numpy as np
import cv2
import time
import pyttsx3
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
camera=cv2.VideoCapture(0)
trained_data=cv2.face.LBPHFaceRecognizer_create()
trained_data.read("C:/Users/rosha/OneDrive/Desktop/Project_internship/trained_Data.yml")
id=0
while(1):
    ret,img=camera.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.4,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=trained_data.predict(gray[y:y+h,x:x+w])    
        if(id==1):
            print("Happy Face")
            pyttsx3.speak("Great!! You're Alright")
            time.sleep(3)
        elif(id==2):
            print("Feeling Sleepy")
            pyttsx3.speak("Let me comfort you so that you can sleep well!!")
            time.sleep(1)
        elif(id==3):
            print("Feeling Sad")
            pyttsx3.speak("Don't feel sad! i'm here to help you!!")
        elif(id==4):
            print("Angry face") 
            pyttsx3.speak("Please! don't be angry,being angry! makes you take wrong decision some time!!")
    cv2.imshow('img',img)
    if cv2.waitKey(1) == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()       
