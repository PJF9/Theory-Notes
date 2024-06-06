import cv2 as cv
import numpy as np



def drawing():
    ## Creating a blank image
    blank = np.zeros((500, 500, 3), dtype="uint8") # (shape=h,w,c, dtype)
    cv.imshow("Img 0", blank)

    ## 1. Painting the Image a certain colour
    blank[99:199, 300:400] = 255,0,0 # b,g,r
    cv.imshow("Img 1", blank)

    ## 2. Draw a rectangle
    cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2) # (image, point_1, point_1, colour, thickness)
    cv.imshow("Img 2", blank)
    
    ### Filling the rectangle
    cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED) # or -1
    cv.imshow("Img 3", blank)

    ### Instead of fixxing values we can use `img.shape[0]` and `img.shape[1]` for height and width respectively

    ## 3. Draw a circle
    cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (0, 0, 255), thickness=3) # (image, center, rad, colour, thickness)
    cv.imshow("Img 4", blank)

    ## 4. Draw a line
    cv.line(blank, (100,300), (200,400), (255,255,255), thickness=2) # (image, point_1, point_1, colour, thickness)
    cv.imshow("Img 5", blank)

    ## 5. Writing Text to an image
    cv.putText(blank, "Hello, my name is PJ!!!", (40,50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,255), thickness=2) # (image, text, origin, font, font_scale, colour, thickness)
    cv.imshow("Img 6", blank)

    cv.waitKey(0)


if __name__ == "__main__":
    drawing()
