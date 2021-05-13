# coding: utf-8
# Team : Quality Management Center
# Author：RuiqingY
# Date ：2021/5/13 17:18
# Tool ：PyCharm


import os
import cv2

datapath = "data/"
# img = cv2.imread("1.jpg")
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
face_cascade.load("haarcascade_frontalface_alt2.xml")

for img in os.listdir(datapath):
    frame = cv2.imread(datapath+img)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0),2)
        # cv2.imshow("img",img)
        # cv2.waitKey()
    imgs = img.split('.')
    cv2.imwrite("result/"+imgs[0]+"_result.jpg",frame)