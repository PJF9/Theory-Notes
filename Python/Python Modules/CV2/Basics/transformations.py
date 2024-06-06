import cv2 as cv
import numpy as np


def translate(img, x, y):
    """
    x, y the numbers of pixels we want the images to be shifted on the x and y axis respectively
        -x --> Left
        -y --> Up
        x --> Right
        y --> Down
    """
    trans_mat = np.float32([[1,0,x], [0,1,y]])

    dims = (img.shape[1], img.shape[0]) # (width, height)

    return cv.warpAffine(img, trans_mat, dims)


def rotate(img, angle, rotation_point=None):
    """
    angle > 0: counter clock wise
    angle < 0: clock wise
    """

    height, width = img.shape[:2]

    ## Rotating with respect to the middle of the image
    if rotation_point is None:
        rotation_point = (width//2, height//2)

    rot_mat = cv.getRotationMatrix2D(rotation_point, angle, 1.0)

    dims = (width, height)

    return cv.warpAffine(img, rot_mat, dims)


def transformations():
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\park.jpg")
    cv.imshow("Image 1", img)

    ## Shifting the Image (Translation)
    t = translate(img, 100, 100)
    # cv.imshow("Image 2", t)

    ## Rotating the Image
    r = rotate(img, -45)
    # cv.imshow("Image 3", r)

    ## Flipping the image
    f = cv.flip(img, -1) # (image, flip_code)
    cv.imshow("Image 4", f)

    ### 0: flipping the image on the x axis | 1: flipping the image on the y axis | -1: flipping the image both on x and y axis

    cv.waitKey(0)


if __name__ == "__main__":
    transformations()
