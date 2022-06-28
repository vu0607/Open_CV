import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')
people = ['Tung_Duong', 'Ha_Anh_Tuan']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'105180399.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Picture', gray)

#Face detection 
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=3)

for(x,y,h,w) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with confidence of {confidence}')
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2 )
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Recognition face', img)
cv.waitKey()
    