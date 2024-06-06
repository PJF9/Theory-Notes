import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def computing_histograms():
    ## Visaluzing the pixel intensity distribution of the image

    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\cats.jpg")
    cv.imshow("Image 1", img)

    blank = np.zeros(img.shape[:2], dtype="uint8")

    mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
    masked = cv.bitwise_and(img,img,mask=mask)
    cv.imshow("Mask", masked)

    plt.figure()
    plt.title("Colour Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")
    colors = ("b", "g", "r")
    for i,col in enumerate(colors):
        hist = cv.calcHist([img], [i], mask, [256], [0,256]) # (images, index of channel we want to compute histogram for, mask can be None, hist_size, ranges)
        plt.plot(hist, color=col)
        plt.xlim([0,256])
    
    plt.show()

    ## Can also compute histograms for gray scale images

    cv.waitKey(0)


if __name__ == "__main__":
    computing_histograms()
