import os
import pickle
import uuid

import cv2
import face_recognition
import imutils
import numpy as np
from flask import Flask, request, jsonify
import  base64

app = Flask(__name__)
@app.route("/Criminal",methods=['Post'])
def Criminal():
    date = request.form['billal']
    imgdata =base64.b64decode(date)
    path_file = ('People_image/%s.jpg' % uuid.uuid4().hex)
    with open(path_file,'wb')as f:
        f.write(imgdata)
    frame = cv2.imread(path_file)
    data = pickle.loads(open("criminal.pickle", "rb").read())
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(frame, width=750)
    r = frame.shape[1] / float(rgb.shape[1])
    boxes = face_recognition.face_locations(rgb,
                                            model="hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(data["encodings"],
                                                 encoding)
        faceDis = face_recognition.face_distance(data["encodings"],
                                                 encoding)
        matchIndex = np.argmin(faceDis)
        if True in matches and faceDis[matchIndex] < 0.50:
            finalid = int(data["names"][matchIndex])
        else:
            finalid = "UnKnown"

    print(finalid)
    os.remove(path_file)
    return jsonify({'error':'false','result':finalid})
@app.route("/Missing",methods=['Post'])
def Missing():
    date = request.form['billal']
    imgdata =base64.b64decode(date)
    path_file = ('People_image/%s.jpg' % uuid.uuid4().hex)
    with open(path_file,'wb')as f:
        f.write(imgdata)
    frame = cv2.imread(path_file)
    data = pickle.loads(open("criminal.pickle", "rb").read())
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(frame, width=750)
    r = frame.shape[1] / float(rgb.shape[1])
    boxes = face_recognition.face_locations(rgb,
                                            model="hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(data["encodings"],
                                                 encoding)
        faceDis = face_recognition.face_distance(data["encodings"],
                                                 encoding)
        matchIndex = np.argmin(faceDis)
        if True in matches and faceDis[matchIndex] < 0.50:
            finalid = int(data["names"][matchIndex])
        else:
            finalid = "UnKnown"
    print(finalid)
    os.remove(path_file)
    return jsonify({'error':'false','result':finalid})
@app.route("/Person",methods=['Post'])
def Person():
    date = request.form['billal']
    imgdata =base64.b64decode(date)
    path_file = ('People_image/%s.jpg' % uuid.uuid4().hex)
    with open(path_file,'wb')as f:
        f.write(imgdata)
    frame = cv2.imread(path_file)
    data = pickle.loads(open("People.pickle", "rb").read())
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(frame, width=750)
    r = frame.shape[1] / float(rgb.shape[1])
    boxes = face_recognition.face_locations(rgb,
                                            model="hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(data["encodings"],
                                                 encoding)
        faceDis = face_recognition.face_distance(data["encodings"],
                                                 encoding)
        matchIndex = np.argmin(faceDis)
        if True in matches and faceDis[matchIndex] < 0.50:
            finalid = int(data["names"][matchIndex])
        else:
            finalid = "UnKnown"
    print(finalid)
    os.remove(path_file)
    return jsonify({'error':'false','result':finalid})
@app.route("/Officer",methods=['Post'])
def Officer():
    date = request.form['billal']
    imgdata =base64.b64decode(date)
    path_file = ('People_image/%s.jpg' % uuid.uuid4().hex)
    with open(path_file,'wb')as f:
        f.write(imgdata)
    frame = cv2.imread(path_file)
    data = pickle.loads(open("Employee.pickle", "rb").read())
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(frame, width=750)
    r = frame.shape[1] / float(rgb.shape[1])
    boxes = face_recognition.face_locations(rgb,
                                            model="hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(data["encodings"],
                                                 encoding)
        faceDis = face_recognition.face_distance(data["encodings"],
                                                 encoding)
        matchIndex = np.argmin(faceDis)
        if True in matches and faceDis[matchIndex] < 0.50:
            finalid = int(data["names"][matchIndex])
        else:
            finalid = "UnKnown"
    print(finalid)
    os.remove(path_file)
    return jsonify({'error':'false','result':finalid})
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True,)