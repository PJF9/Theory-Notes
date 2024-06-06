import cv2 as cv
import numpy as np


def split_merge_channels():
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\park.jpg")
    cv.imshow("Image 1", img)

    ## Splitting the Image to its channels
    blank = np.zeros(img.shape[:2], dtype="uint8")

    b, g, r = cv.split(img)

    blue = cv.merge([b,blank,blank])
    green = cv.merge([blank,g,blank])
    red = cv.merge([blank,blank,r])

    cv.imshow("Blue", blue)
    cv.imshow("Green", green)
    cv.imshow("Red", red)

    merged = cv.merge([b,g,r])
    cv.imshow('Merged Image', merged)

    cv.waitKey(0)


if __name__ == "__main__":
    split_merge_channels()
