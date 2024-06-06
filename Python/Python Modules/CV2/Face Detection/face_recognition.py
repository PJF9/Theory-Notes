import cv2 as cv
import numpy as np


def recognition():
    haar_cascade = cv.CascadeClassifier("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Face Detection\\files\\haar_face.xml")

    people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]

    ## Initalize the Face Recognizer
    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Face Detection\\files\\face_trained.yml")

    ## Getting an image
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Faces\\val\\ben_afflek\\2.jpg")

    ## Detect the face in the image
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)

        print(f"Label = {people[label]} with a confidence of {confidence}")

        ## Write some text on the image
        cv.putText(img, str(people[label]), (30,30), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

        cv.imshow("Detected Face", img)
    
    cv.waitKey(0)


if __name__ == "__main__":
    recognition()
