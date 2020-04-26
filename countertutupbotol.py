import numpy as np
import cv2 as cv

import sys

def main():
    fn = 'img/botol.jpg'

    src = cv.imread(fn)
    img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(img, 5)
    cimg = src.copy() # numpy function

    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 10, np.array([]), 69, 21, 9, 26)

    counter = 0
    if circles is not None: # Check if circles have been found and only then iterate over these and add them to the image
        _a, b, _c = circles.shape
        for i in range(b):
            cv.circle(
                cimg, (circles[0][i][0], 
                circles[0][i][1]), 
                circles[0][i][2], 
                (0, 0, 255), 2, cv.LINE_AA
                    )
            cv.circle(
                cimg, (circles[0][i][0], 
                circles[0][i][1]), 2, 
                (0, 255, 0), 3, cv.LINE_AA
                    )  # draw center of circle
            counter += 1

        print(f'counter ;', counter)
        cv.imshow("detected circles", cimg)

    cv.imshow("source", src)
    cv.waitKey(0)
    print('Done')


if __name__ == '__main__':
    main()
    cv.destroyAllWindows()