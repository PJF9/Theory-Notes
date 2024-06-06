import numpy as np
import cv2 as cv
import os



def train():
    people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]
    DIR = "C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Faces\\train"

    haar_cascade = cv.CascadeClassifier("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Face Detection\\files\\haar_face.xml")

    ## Converting the Images to array and capture them as features
    features = []
    labels = []
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        ### For every image on the name folder
        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            ### Convert the image to array
            img_array = cv.imread(img_path)
            if img_array is None:
                continue 
            
            ### Convert the image to gray scale
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            ### Detect the faces on the image
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            ### Crop the faces of every image
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

    print(f"Length of the features: {len(features)}")
    print(f"Length of the labels: {len(labels)}")

    features = np.array(features, dtype="object")
    labels = np.array(labels)

    ## Initialize the face recognizer
    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    ## Train the Recognizer on the features list and the labels list
    face_recognizer.train(features, labels)

    ## Save the Trained parameters and data 
    face_recognizer.save("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Face Detection\\files\\face_trained.yml")
    np.save("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Face Detection\\files\\features.npy", features)
    np.save("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Face Detection\\files\\labels.npy", labels)


if __name__ == "__main__":
    train()
