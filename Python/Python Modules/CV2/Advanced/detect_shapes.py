import cv2 as cv
import numpy as np


## We need also a copy of the image because in `img_contour` we are going to write upon
def get_contours(img, img_contour):
    ## Finding the Conotur points of the image
    contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        ## Finding the area of the contour
        area = cv.contourArea(cnt)

        ## `500` is hard-coded
        if (area > 500):
            ## Drawing the Contours to the image
            cv.drawContours(img_contour, cnt, -1, (255, 0, 0), thickness=3) # `-1` to draw all the contours

            ## Finding the Length of the contour
            perimeter = cv.arcLength(cnt, closed=True)
            
            ## Approximate the Conour by using points
            approx = cv.approxPolyDP(cnt, 0.02*perimeter, closed=True)

            ## With the length of points we can have an idea what the shape is
            contour_type_points = len(approx)

            ## Getting the points of the bounding box, if we wanted to create a bounding box around the object
            x, y, w, h = cv.boundingRect(approx)

            ## Placing a box using the bounding points
            cv.rectangle(img_contour, (x, y), (x+w, y+h), (0, 255 ,0), thickness=2)

            ## Identifying the type of the object
            if (contour_type_points == 3):
                object_type ="Tri"

            elif (contour_type_points == 4):
                ## On square: width/height = 1, so we check the aspect ratio
                asp_ratio = w/float(h)

                if (asp_ratio > 0.98) and (asp_ratio < 1.03):
                    object_type= "Square"
                else:
                    object_type="Rectangle"

            elif (contour_type_points > 4):
                object_type= "Circles"

            else:
                object_type="None"

            ## Writing the type of the object to the image (around the center of the image)
            cv.putText(img_contour, object_type, (x+(w//2)-30, y+(h//2)+10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), thickness=2)


def resize_images(img, scale):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dims = (width, height)

    return cv.resize(img, dims, interpolation=cv.INTER_AREA)


def detect():
    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\shapes.png")
    cv.imshow("Image 1", img)

    img_contour = img.copy()

    ## Finding the edges of the image
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(img_gray, (7,7), 1)
    img_canny = cv.Canny(img_blur, 50, 50)
    
    get_contours(img_canny, img_contour)

    ## For Display the image in a 3x3 grid
    img_blank = np.zeros_like(img)

    ## For displaying all images together
    gray_3c = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)
    blur_3c = cv.cvtColor(img_blur, cv.COLOR_GRAY2BGR)
    canny_ec = cv.cvtColor(img_canny, cv.COLOR_GRAY2BGR)

    ## Resizing the Images before displaying int othe grid to fit them in my monitor
    img = resize_images(img, scale=0.6)
    gray_3c = resize_images(gray_3c, scale=0.6)
    blur_3c = resize_images(blur_3c, scale=0.6)
    canny_ec = resize_images(canny_ec, scale=0.6)
    img_contour = resize_images(img_contour, scale=0.6)
    img_blank = resize_images(img_blank, scale=0.6)

    stack_1 = np.hstack((img, gray_3c, blur_3c))
    stack_2 = np.hstack((canny_ec, img_contour, img_blank))
    stack = np.vstack((stack_1, stack_2))

    cv.imshow("Stack", stack)

    cv.waitKey(0)


if __name__ == "__main__":
    detect()
