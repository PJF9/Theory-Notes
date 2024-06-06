import cv2 as cv


def change_color_spaces():
    ## Changing an image from one color space (like gbr) to another (like gray scale)

    img = cv.imread("C:\\Users\\jacob\\Documents\\Programming\\Projects\\Work In Progress\\NAS\\CV2\\Resources\\Photos\\park.jpg")
    cv.imshow("Image 1", img)

    ## BGR to Grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", gray)

    ## BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow("HSV", hsv)

    ## BGR to L*a*b
    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    cv.imshow("LAB", lab)

    ## BGR to RGB
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imshow("RGB", rgb)

    ## HSV to BGR
    lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
    cv.imshow("LAB --> BGR", lab_bgr)

    cv.waitKey(0)


if __name__ == "__main__":
    change_color_spaces()
