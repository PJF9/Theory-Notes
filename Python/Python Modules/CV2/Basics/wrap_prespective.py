import cv2 as cv
import numpy as np


def wrap():
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\cards.jpg")
    cv.imshow("Image 1", img)

    ## Finding the Points of the object we want to wrapt
    pts1 = np.float32([[111,219], [287,188], [154,482], [352,440]])
    pts2 = np.float32([[0,0], [img.shape[1],0], [0,img.shape[0]], [img.shape[1],img.shape[0]]])

    ## Get the Object
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    output = cv.warpPerspective(img, matrix, (img.shape[1], img.shape[0]))

    cv.imshow("Image 2", output)

    cv.waitKey(0)


if __name__ == "__main__":
    wrap()
