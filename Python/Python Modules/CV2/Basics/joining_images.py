import cv2 as cv
import numpy as np


def join():
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\cat.jpg")
    cv.imshow("Image 1", img)

    img_hor = np.hstack((img, img))
    cv.imshow("Image 2", img_hor)

    scaled_img = np.vstack((img_hor, img_hor))
    cv.imshow("Image 3", scaled_img)

    cv.waitKey(0)


if __name__ == "__main__":
    join()
