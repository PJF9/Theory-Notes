import cv2 as cv
import numpy as np


def mask():
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\cats 2.jpg")
    cv.imshow("Image 1", img)

    ## Creating the Mask
    blank = np.zeros(img.shape[:2], dtype="uint8")

    circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
    rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
    final_shape = cv.bitwise_and(circle,rectangle)

    cv.imshow("Shape", final_shape)

    ## Apply the Mask
    masked = cv.bitwise_and(img,img,mask=final_shape)
    cv.imshow("Masked Image", masked)

    cv.waitKey(0)


if __name__ == "__main__":
    mask()
