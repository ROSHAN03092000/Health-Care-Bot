#Coded and presented by: Roshan Ravi Kumar Shetti
#From:RV Institute of technology and management
#Under the guidance of Yashwant sir
#From: Loginware


import os
import numpy as np
import cv2
from PIL import Image
recognizer=cv2.face.LBPHFaceRecognizer_create()
path="C:/Users/rosha/OneDrive/Desktop/Project_internship/Data"
def fun1(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    nums=[]
    for imagePath in imagePaths:
        faceimg=Image.open(imagePath).convert("L")
        facenp=np.array(faceimg,"uint8")
        num = int(os.path.split(imagePath)[-1].split(".")[1])
        print(num)
        faces.append(facenp)
        nums.append(num)
        cv2.imshow("Trained dataset",facenp)
        cv2.waitKey(10)
    return np.array(nums),faces
Nums,Faces=fun1(path)
recognizer.train(Faces,Nums)
recognizer.save("C:/Users/rosha/OneDrive/Desktop/Project_internship/trained_Data.yml")
cv2.destroyAllWindows()