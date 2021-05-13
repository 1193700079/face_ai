# coding: utf-8
# Team : Quality Management Center
# Author：RuiqingY
# Date ：2021/5/13 17:18
# Tool ：PyCharm


import os
import cv2

img = cv2.imread("1.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
face_cascade.load("haarcascade_frontalface_alt2.xml")

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for(x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0),2)
    # imshow 和 waitkey 一起使用！
    cv2.imshow("img",img)
    cv2.waitKey()
