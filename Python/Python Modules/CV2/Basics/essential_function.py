import cv2 as cv


def functions():
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\park.jpg")
    cv.imshow("Image 1", img)

    ## Converting to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # (image, colour code)
    cv.imshow("Image 2", gray)

    ## Blur an image
    blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # (image, kernel_size)
    cv.imshow("Image 3", blur)

    ## Finding the edges that are present in the image
    canny = cv.Canny(img, 175, 200) # (image, threshhold_1, threshhold_1)
    cv.imshow("Image 4", canny)

    ### We can reduce the edges by passing the blur image

    ## Dilating the edges of an image
    dilated = cv.dilate(canny, (7,7), iterations=3) # (image, kernel size, iterations)
    cv.imshow("Image 5", dilated)

    ## Getting back the edges from a dilated image
    eroded = cv.erode(dilated, (7,7), iterations=3) ## (image, kernel_size, iterations)
    cv.imshow("Image 6", eroded)

    ## Resizing and Croping an Image
    resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) # (image, destination size, interpolation)
    cv.imshow("Image 7", resize)

    ### cv.INTER_AREA: for downsizing an image | cv.INTER_LINEAR for upsizing an image | cv.INTER_CUBIC for upsizing better but slowest

    croped = img[50:200, 200:400]
    cv.imshow("Image 8", croped)


    cv.waitKey(0)


if __name__ == "__main__":
    functions()
