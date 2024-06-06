import cv2 as cv
import numpy as np


def rescale_frame(frame, scale=0.75):
    ## Changing the Width and the Height of the Frame
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dims = (width, height)

    return cv.resize(frame, dims, interpolation=cv.INTER_AREA)


def color():
    path = "C:\\Users\\jacob\\Documents\\Programming\\Theory\\Python\\Python Modules\\CV2\\Resources\\Photos\\lambo.png"

    ## Create tje Track Bars so we can change the different colours
    cv.namedWindow("TrackBars")
    cv.resizeWindow("TrackBars", 640, 240)
    cv.createTrackbar("Hue Min", "TrackBars", 0, 179, lambda a: None)
    cv.createTrackbar("Hue Max", "TrackBars", 19, 179, lambda a: None)
    cv.createTrackbar("Sat Min", "TrackBars", 110, 255, lambda a: None)
    cv.createTrackbar("Sat Max", "TrackBars", 240, 255, lambda a: None)
    cv.createTrackbar("Val Min", "TrackBars", 153, 255, lambda a: None)
    cv.createTrackbar("Val Max", "TrackBars", 255, 255, lambda a: None)

    try:
        while True:
            img = cv.imread(path)

            ## Convberting the Image to HSV
            img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

            ## Get the Trackbar values
            h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
            h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
            s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
            s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
            v_min = cv.getTrackbarPos("Val Min", "TrackBars")
            v_max = cv.getTrackbarPos("Val Max", "TrackBars")

            print(f"H(min): {h_min} | H(max): {h_max} | S(min): {s_min} | S(max): {s_max} | V(min): {v_min} | V(max): {v_max}")
            
            ## Creating the Mask
            lower = np.array([h_min, s_min, v_min])
            upper = np.array([h_max, s_max, v_max])
            mask = cv.inRange(img_HSV, lower, upper)
            mask_3c = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)

            ## Applying the Mask to change the colors
            result = cv.bitwise_and(img, img, mask=mask)

            img = rescale_frame(img, scale=0.5)
            img_HSV = rescale_frame(img_HSV, scale=0.5)
            mask_3c = rescale_frame(mask_3c, scale=0.5)
            result = rescale_frame(result, scale=0.5)

            ## Stacking the Images together
            stack_img_1 = np.hstack((img, img_HSV))
            stack_img_2 = np.hstack((mask_3c, result))
            stack_img = np.vstack((stack_img_1, stack_img_2))

            cv.imshow("Images", stack_img)


            cv.waitKey(1)
    except cv.error:
        pass


if __name__ == "__main__":
    color()
