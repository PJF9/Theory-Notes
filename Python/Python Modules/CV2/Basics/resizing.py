import cv2 as cv


def rescale_frame(frame, scale=0.75):
    ## Changing the Width and the Height of the Frame
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dims = (width, height)

    return cv.resize(frame, dims, interpolation=cv.INTER_AREA)


## Only works for live video using an external camera
def change_video_resolution(capture, width, height):
    ## Set different width and height to the capture object
    capture.set(3, width)
    capture.set(4, height)


def resize_images():
    ## Reading the image
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\cat_large.jpg")

    ## Resizing the image
    scaled_img = rescale_frame(img, scale=0.5)

    ## Displaying the Image (as a new window)
    cv.imshow("Cat Resized", scaled_img)

    cv.waitKey(0)


def resizing_video():
    capture = cv.VideoCapture("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Videos\\dog.mp4")

    ## Reading the video frame by frame
    while True:
        is_true, frame = capture.read()

        if is_true:
            ## Resizing the video's frames
            scaled_frame = rescale_frame(frame)

            cv.imshow("Video", frame)
            cv.imshow("Video Resize", scaled_frame)

            ## Breaking the Loop
            if cv.waitKey(20) and (0xFF == ord('d')):
                break
        else:
            break

    capture.release()
    cv.destroyAllWindows()


def live_footage():
    capture = cv.VideoCapture(0)

    change_video_resolution(capture, 720, 720)

    while True:
        is_true, frame = capture.read()

        if is_true:
            cv.imshow("Video", frame)

            ## Breaking the Loop with any key
            if cv.waitKey(1) != -1:
                break
        else:
            break

    capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    live_footage()
