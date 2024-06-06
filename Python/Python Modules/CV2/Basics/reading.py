import cv2 as cv


def reading_images():
    ## Reading the Image
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\cats.jpg")

    ## Reading a larger image (it's larger than the screen)
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\cat_large.jpg")

    ## Displaying the Image (as a new window)
    cv.imshow("Cats", img) # (name of the window, pixels to display)

    ## Waiting for infinite amount of time before closing the window
    cv.waitKey(0)


def reading_videos():
    """
    For reading videos we need to create a `Capture` obejct.
    The arguments can be either an index indicating the index of the camera you want to capture
    video from, or the path of the video you want to read

    For camera reading we need to specify the width and the height. We can do this with:
        capture.set(3, width)
        capture.set(4, height)
    after initializing the capture object

    We can also change the brightness:
        captrue.set(10, brightness)
    """
    capture = cv.VideoCapture("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Videos\\dog.mp4")

    ## Reading the video frame by frame
    while True:
        success, frame = capture.read() # (succesfully read the frame, the actual frame)

        if success:
            cv.imshow("Video", frame)

            ## Breaking the Loop
            if cv.waitKey(20) and (0xFF == ord("q")):
                break
        else:
            break

    ## Release the capture pointer
    capture.release()
    ## Destroy all windows
    cv.destroyAllWindows()



if __name__ == "__main__":
    reading_videos()
