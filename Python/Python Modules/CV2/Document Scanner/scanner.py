import cv2 as cv
import numpy as np


def resize_images(img, scale):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dims = (width, height)

    return cv.resize(img, dims, interpolation=cv.INTER_AREA)


def pre_processing(img):
    ## Finding the edges of the image
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(img_gray, (5,5), 1)
    img_canny = cv.Canny(img_blur, 200, 200)

    ## Dilating and Eroding the image with the edges
    kernel = np.ones((5,5))
    img_dial = cv.dilate(img_canny, kernel, iterations=2)
    img_thres = cv.erode(img_dial, kernel, iterations=1)
    
    return img_thres


def get_contours(img, img_contour):
    ## Finding the bigget contour of the screen
    contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    
    biggest = np.array([])
    maxArea = 0
    for cnt in contours:
        area = cv.contourArea(cnt)
    
        if (area > 5000):
            peri = cv.arcLength(cnt, closed=True)
            approx = cv.approxPolyDP(cnt, 0.02*peri, closed=True)
            
            if (area > maxArea) and (len(approx) == 4):
                biggest = approx
                maxArea = area

    cv.drawContours(img_contour, biggest, -1, (255, 0, 0), 20)

    return biggest


def reorder(my_points):
    ## Reshaping the points from (2, 4) -> (4, 2)
    my_points = my_points.reshape((4,2))

    my_points_new = np.zeros((4,1,2),np.int32)

    ## The point(0,0) has the lowest sum (x + y) | the point_(w, h) has the maximum
    add = my_points.sum(1)
    my_points_new[0] = my_points[np.argmin(add)]
    my_points_new[3] = my_points[np.argmax(add)]
    
    ## The point(w, 0) has the minimum y - x | the point(0, h) has the maximum
    diff = np.diff(my_points, axis=1)
    my_points_new[1]= my_points[np.argmin(diff)]
    my_points_new[2] = my_points[np.argmax(diff)]

    return my_points_new


def get_warp(img, biggest):
    width_img = 540
    height_mg = 640

    ## Reshaping the points of the biggest contour in order to create the warp prespective matrix
    biggest = reorder(biggest)

    ## Getting the Wrap Prespective by the points
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [width_img, 0], [0, height_mg], [width_img, height_mg]]) # this point give us the format that the first point should have
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv.warpPerspective(img, matrix, (width_img, height_mg))
    
    return imgOutput


def main():
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\document.jpg")
    img = resize_images(img, 0.4)

    ## Creating the image where we will draw the contours
    img_contour = img.copy()
    
    ## Converting the image into binary via threshold values
    img_thresh = pre_processing(img)

    ## Get the biggest contour of the screen
    biggest = get_contours(img_thresh, img_contour)

    ## Adding colour channels to the binary image for display
    img_thresh = cv.cvtColor(img_thresh, cv.COLOR_GRAY2BGR)

    ## If found contour
    if biggest.size != 0:
        img_warped = get_warp(img, biggest)

        ## Reshaping the wrap images for display
        img_warped = cv.resize(img_warped, (480, 640), interpolation=cv.INTER_AREA)

        image_array = ([img, img_thresh, img_contour, img_warped])
    else:
        image_array = ([img, img_thresh, img_contour, np.zeros((480, 360, 3), dtype="uint8")])

    stack = np.hstack(image_array)
    cv.imshow("Images", stack)

    cv.waitKey(0)


if __name__ == "__main__":
    main()
