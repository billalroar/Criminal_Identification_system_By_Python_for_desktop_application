import os
import pickle

import cv2
import numpy as np
import face_recognition

# known_image = face_recognition.load_image_file('People_image/saiful_3.jpg')
# unknown_image = face_recognition.load_image_file('People_image/saiful_4.jpg')
#
# biden_encoding = face_recognition.face_encodings(known_image)[0]
# print(biden_encoding)
# unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
# print(unknown_encoding)
#
# results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
# print(results)
encodingsBox = []
namesBox = []
imagePaths = [os.path.join("People_image_identify", f) for f in os.listdir("People_image_identify")]
for imagePath in imagePaths:
    frame = cv2.imread(imagePath)
    Id = int(os.path.split(imagePath)[-1].split(".")[1])
    print(Id)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb_frame, model="hog")
    encodings = face_recognition.face_encodings(rgb_frame, boxes)
    for encoding in encodings:
        encodingsBox.append(encoding)
        namesBox.append(Id)
        data = {"encodings": encodingsBox, "names": namesBox}
f = open("People.pickle", "wb")
f.write(pickle.dumps(data))
f.close()


