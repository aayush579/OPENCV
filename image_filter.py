import cv2
import numpy as np

img = cv2.imread('parrot.jpg')


sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sherr = cv2.filter2D(img,-1,sharpen_kernel)
cv2.imshow('sharpened',sherr)
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

blurred = cv2.medianBlur(sherr,5)
cv2.imshow('blurred',blurred)
cv2.imshow('original',sherr)
cv2.waitKey(0)
cv2.destroyAllWindows()
