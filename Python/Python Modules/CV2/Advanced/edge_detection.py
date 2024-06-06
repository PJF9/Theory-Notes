import cv2 as cv
import numpy as np


def detect():
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\park.jpg")
    cv.imshow("Image 1", img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ## 1. Laplacian
    lap = cv.Laplacian(gray, cv.CV_64F) # (image, depth)
    lap = np.uint8(np.absolute(lap))
    cv.imshow("Laplacian", lap)

    ## 2. Sobel
    sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0) # (image, depth, dx, dy)
    sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)

    cv.imshow("Sobel X", sobel_x)
    cv.imshow("Sobel Y", sobel_y)

    combined_sobel = cv.bitwise_or(sobel_x, sobel_y)
    cv.imshow("Sobel", combined_sobel)

    ## 3. Canny
    canny = cv.Canny(gray, 150, 175)
    cv.imshow("Canny", canny)

    cv.waitKey(0)


if __name__ == "__main__":
    detect()
