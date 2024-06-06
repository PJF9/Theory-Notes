import cv2 as cv
import numpy as np


def camera_config(capture, frame_width, frame_height, brightness):
    capture.set(3, frame_width)
    capture.set(4, frame_height)
    capture.set(10, brightness)


## Finding the color in each frame
def find_colors(img, img_result, my_colors, my_color_values):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    count = 0
    newPoints = []
    for color in my_colors:
        ## Creating the Mask for each color
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV, lower, upper)

        ## Finding the condours of the mask
        x, y = get_contours(mask)

        ## Draw a cicrle at the returned contour location
        cv.circle(img_result, (x,y), 15, my_color_values[count], cv.FILLED)
        count += 1

        ## Add the points in order to write them into the image
        if (x != 0) and (y != 0):
            newPoints.append([x, y, count])

    return newPoints


def get_contours(img):
    contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    x, y, w = 0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
    
        if (area > 500):
            peri = cv.arcLength(cnt, closed=True)
            approx = cv.approxPolyDP(cnt, 0.02*peri, closed=True)

            x, y, w, _ = cv.boundingRect(approx)

    return x+w//2, y ## return the top and center point of the detected contour


def draw_on_canvas(img_result, my_points, my_color_values):
    ## Draw a point to the image
    for point in my_points:
        cv.circle(img_result, (point[0], point[1]), 10, my_color_values[point[2]], cv.FILLED)


def main():
    ## We need to set the colors that the app will identify (use the `color_picker.py` file)
    my_colors = [
        [58, 98, 102, 76, 255, 144], # H(min), S(min), V(min), H(max), S(max), V(max)
        [107, 124, 0, 131, 255, 255]
    ]
    ### BGR values of the above colors
    my_color_values = [
        [0, 255, 0],
        [255, 0, 0]
    ]
    my_points =  []  ## [x, y, colorId]
    
    ## Setting the camera capture pointer
    capture = cv.VideoCapture(0)
    camera_config(capture, 640, 480, 150)

    while True:
        success, img = capture.read()
        if (success):
            img_result = img.copy()

            ## Collect the point that need to be written into the image
            new_points = find_colors(img, img_result, my_colors, my_color_values)

            if len(new_points) != 0:
                for newP in new_points:
                    my_points.append(newP)

            if len(my_points) != 0:
                draw_on_canvas(img_result, my_points, my_color_values)

            cv.imshow("Result", img_result)
            
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
