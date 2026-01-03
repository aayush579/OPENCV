import pandas as pd
import cv2

image = cv2.imread('parrot.jpg') # read image

if image is not None:
    print(("Image loaded"))
else:
    print(("Image not loaded"))


cv2.imshow("Image", image) #display image
cv2.waitKey(0) #loop  to wait the windows till key is pressed
cv2.destroyAllWindows()

cv2.imwrite("parrot.jpg", image)  #to download a image using opencv

if image is not None:
    H,W,C = image.shape # image scale readijng
    print(f"Image loaded: \n Height: {H} \n Width: {W} \n Channels: {C}")
else:
    print("Image not loaded")


#gray scale conversion
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow(" GrayScale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

