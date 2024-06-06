import cv2 as cv


def detect_faces(path):
    img = cv.imread(path)

    ## Convert the Image to Gray Scale to reduce complexity and colors
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ## Initialize the Classifier
    haar_cascade = cv.CascadeClassifier("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Face Detection\\files\\haar_face.xml")

    ## Detecting the Faces
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    print(f"Number of faces found = {len(faces_rect)}")

    ## Drawing the Face Boxes
    for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow("Detected Faces", img)

    cv.waitKey(0)


if __name__ == "__main__":
    detect_faces("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\lady.jpg")
    detect_faces("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\group 2.jpg")
    detect_faces("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\group 1.jpg")

    """
    We can also use the same technique to videos by detecting haar cascades to every
    frame and drawing the boxes for every frame
    """
