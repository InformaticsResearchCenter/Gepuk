import numpy as np
import cv2 

cv2.startWindowThread()
#showing image with RGB
img = cv2.imread('img/img1.jpg',cv2.IMREAD_COLOR)

#showing gray image not RGB
#img = cv2.imread('img/img1.jpg',0)


 
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()