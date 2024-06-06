import cv2 as cv


def blur_techniques():
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\cats.jpg")
    cv.imshow("Image 1", img)

    ## 1. Averaging
    average = cv.blur(img, (7,7))
    cv.imshow("Average Blur", average)

    ## 2. Gaussian Blur (more natural than the others)
    gauss = cv.GaussianBlur(img, (7,7), 0) # 0: the standard deviation in the x direction
    cv.imshow("Gaussian Blur", gauss)

    ## 3.  Median Blur (it's more effectrive than the others | needs lower kernel size, not 7)
    median = cv.medianBlur(img, 7)
    cv.imshow("Median Blur", median)

    ## 4.  Bilateral (even more effective than median | retains the edges of the image)
    bilateral = cv.bilateralFilter(img, 14, 35, 25) # (image, diameter, sigma_colour, sigma_space) | larger values of neigbour sigmas will influence the given pixel
    cv.imshow("Bilateral", bilateral)

    cv.waitKey(0)


if __name__ == "__main__":
    blur_techniques()
