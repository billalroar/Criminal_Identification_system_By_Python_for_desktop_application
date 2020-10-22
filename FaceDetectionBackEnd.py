import os.path
import numpy as np
import cv2
import json
from flask import  request,Flask,Response
import  uuid

#function detect face from image
def faceDectect(img1):
    # save file
    path_file = ('static/%s.jpg' % uuid.uuid4().hex)
    cv2.imwrite(path_file, img1)

    # start face identification use images
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainner.yml')
    facedetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    img2 = cv2.imread(path_file)
    jsonlist={path_file:"%s"%path_file}
    img = cv2.resize(img2, (700, 900), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facedetector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30),)
    print("yes")

    for (x, y, w, h) in faces:
        print("yes1")

        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        if (conf < 50):
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            if (Id == 1):
                Id = "Anirban"
                print(Id)
            elif (Id == 2):
                Id = "billal"
                print(Id)
        else:
            Id = "Unknown"
            continue

        print("yes2")
        cv2.putText(img, str(Id), (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        print("yes3")
    cv2.imshow('frame', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return json.dumps(jsonlist)  # return image file name



#API
app= Flask(__name__)

#route http post to this method
@app.route("/upload",methods=['POST'])
def up():
    #retrieve image from client
    img = cv2.imdecode(np.fromstring(request.files['billal'].read(),np.uint8),cv2.IMREAD_UNCHANGED)
    #process image
    img_processed = faceDectect(img)
    #responce
    return Response(response=img_processed,status=200,mimetype="application/json")#return json string


#start server
if __name__ =="__main__":
 app.run(host='0.0.0.0',port=5000,debug=True,)
