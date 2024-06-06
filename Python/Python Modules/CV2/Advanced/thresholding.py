import cv2 as cv


def thresh():
    ## Convert the Image to a Bianry Image (pixels either 0 or 255)

    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\cats.jpg")
    cv.imshow("Image 1", img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ## Simple Thresholding
    threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) ## threshold value: 150 | all pixels higher than this one will be 255
    cv.imshow("Simple Thresholded", thresh)

    ### `threshold`` is the threshold, meaning the value 150
    print(threshold)

    _, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
    cv.imshow("Simple Thresholded Inverse", thresh_inv)

    ## Adaptive Thresholding (find automaticly the proper threshold value)
    adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 12) # (..., block size, meaning the neigbour size, C for finetune the threshold value)
    cv.imshow("Adaptive Thresholding", adaptive_thresh)

    ## we also have `ADAPTIVE_THRESH_MEAN_C` and other

    cv.waitKey(0)


if __name__ == "__main__":
    thresh()
