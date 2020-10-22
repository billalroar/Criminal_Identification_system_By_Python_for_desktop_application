import cv2
import sys
import numpy as np
from pip._vendor.requests.compat import str


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

# facedetector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# uri = "http://192.168.0.100:8080/video"
# cam = cv2.VideoCapture(uri)
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # faces=faceCascade.detectMultiScale(gray, 1.3,5)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            if(Id==1):
                Id="Anirban"
            elif(Id==2):
                Id="billal"
        else:
            Id="Unknown"
        # cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
        cv2.putText(im,str(Id), (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
    cv2.imshow('im',im)
    if (cv2.waitKey(10)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()