#Coded and presented by: Roshan Ravi Kumar Shetti
#From:RV Institute of technology and management
#Under the guidance of Yashwant sir
#From: Loginware

from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np
global window
import pyttsx3
import time
window=Tk()
window.title("HealthCare")
window.geometry("1000x1000") 
window.configure(bg="blue")
def fun():
    pyttsx3.speak("Welcome to health care!! and i'm health care robo!! and i'm here to make you feel good!!")
    time.sleep(3)
    pyttsx3.speak("Please allow me to capture your facial expression")
def fun1():
    global window1,bent,bent2
    window1=Tk()
    window1.title("Save as")
    window1.geometry("1000x1000")
    window1.configure(bg="violet")
    blab1=Label(window1,text="Enter your Facial Expression:",font=("Relish Pro",30),bg="violet",fg="black")
    blab1.place(x=250,y=300)
    bent=Entry(window1,width=20,font=("Relish Pro",25))
    bent.place(x=300,y=400)
    blab2=Label(window1,text="Enter an Id:",font=("Relish Pro",30),bg="violet",fg="black")
    blab2.place(x=250,y=500)
    btn2=Button(window1,text="Submit",font=("Relish Pro",15),bg="white",fg="blue",width=20,command=fun2)
    btn2.place(x=600,y=700)
    bent2=Entry(window1,width=20,font=("Relish Pro",25))
    bent2.place(x=300,y=600)
    pyttsx3.speak("Please enter your facial expression to train myself")
def fun2():
    global window,window1,bent,bent2
    data=bent.get()
    data_1=bent2.get()
    window1.destroy()
    capt=cv2.VideoCapture(0)
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    i=0
    while(1):
        ret,img=capt.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.4,4)
        for a,b,c,d in faces:
            cv2.imwrite("C:/Users/rosha/OneDrive/Desktop/Project_internship/Data/Image_"+str(data)+str(data_1)+"."+str(i)+".jpg",gray[b:b+d,a:a+c])
            i=i+1
            cv2.rectangle(img,(a,b),(a+c,b+d),(255,0,0),2)
            cv2.imshow("camera",img)
            cv2.waitKey(5)
        if(cv2.waitKey(1) & 0xff==ord("q") or i>50):
            cv2.destroyAllWindows()
            break
    messagebox.showinfo("Message","Data saved successfully!!")
    pyttsx3.speak("data uploaded successfully!")
    window.destroy()         
alab1=Label(window,text="Welcome to Health Care!!",font=("Relish Pro",50),bg="blue",fg="cyan")
alab1.pack()
alab2=Label(window,text="There is no illness that isn't ",font=("Relish Pro",40),bg="blue",fg="violet")
alab3=Label(window,text="exacerbated by stress!! ",font=("Relish Pro",40),bg="blue",fg="violet")
alab4=Label(window,text="I'm here to Help",font=("Relish Pro",40),bg="blue",fg="violet")
alab2.place(x=200,y=300)
alab3.place(x=200,y=360)
alab4.place(x=200,y=420)
btn1=Button(window,text="Click here to capture the image",font=("Relish Pro",20),bg="white",fg="blue",width=25,command=fun1)
btn1.place(x=200,y=680)
fun()
window.mainloop()