import cv2 as cv
import numpy as np


def config(capture, frame_width, frame_height):
    capture.set(3, frame_width)
    capture.set(4, frame_height)


def main():
    ## Setting capure pointer
    capture = cv.VideoCapture(0)
    config(capture, 640, 480)

    ## Setting the Trackbar for picking the right color
    cv.namedWindow("HSV")
    cv.resizeWindow("HSV", 640, 240)
    cv.createTrackbar("HUE Min", "HSV", 0, 179, lambda a: None)
    cv.createTrackbar("HUE Max", "HSV", 179, 179, lambda a: None)
    cv.createTrackbar("SAT Min", "HSV", 0, 255, lambda a: None)
    cv.createTrackbar("SAT Max", "HSV", 255, 255, lambda a: None)
    cv.createTrackbar("VALUE Min", "HSV", 0, 255, lambda a: None)
    cv.createTrackbar("VALUE Max", "HSV", 255, 255, lambda a: None)

    try:
        while True:
            success, img = capture.read()

            if success:
                ## Convert the image into HSV
                img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

                ## Getting the data from the Trackbars
                h_min = cv.getTrackbarPos("HUE Min", "HSV")
                h_max = cv.getTrackbarPos("HUE Max", "HSV")
                s_min = cv.getTrackbarPos("SAT Min", "HSV")
                s_max = cv.getTrackbarPos("SAT Max", "HSV")
                v_min = cv.getTrackbarPos("VALUE Min", "HSV")
                v_max = cv.getTrackbarPos("VALUE Max", "HSV")

                ## Creating the Mask
                lower = np.array([h_min, s_min, v_min])
                upper = np.array([h_max, s_max, v_max])
                mask = cv.inRange(img_HSV, lower, upper)
                
                ## Applying the Mask to get the resulting image
                result = cv.bitwise_and(img, img, mask=mask)

                ## Displaying everything
                mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
                hStack = np.hstack([img, mask, result])
                cv.imshow("Color Picking", hStack)

                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
    except cv.error:
        pass

    capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
