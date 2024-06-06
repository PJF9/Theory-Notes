import cv2 as cv
import numpy as np


def detect():
    ## Detecting the Bountries of objects

    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\cats.jpg")

    cv.imshow("Image 1", img)

    ## 1. Convert the Image to gray scale
    g_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ## 2. Grab the edges of the Image
    canny = cv.Canny(img, 125, 175)

    ## 3. Finding Countours
    contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # (edges, mode, method) | there are alot more modes and methods we can use
    
    ### the function returns a list with all the contour points and the hierarchical representation of those contours

    ### RETR_LIST: returns all the contours detected | RETR_EXTERNAL: returns all the external contours

    print(f"Contours Detected: {len(contours)}")

    ### We can brul blur the image to reduce the number of contours detected

    blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)

    canny = cv.Canny(blur, 125, 175)

    contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    print(f"Contours Detected: {len(contours)}")

    ## 4. Drawing the Contours on the Image
    blank = np.zeros(img.shape, dtype="uint8")

    cv.drawContours(blank, contours, -1, (0,255,0), thickness=1) # (image, contours, contour_index, colour, thickness)
    
    cv.imshow("Image 2", blank)

    cv.waitKey(0)


if __name__ == "__main__":
    detect()
