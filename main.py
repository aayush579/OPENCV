import cv2
img = cv2.imread("parrot.jpg")

# image resizing
if img is not None:
    print("Image Loaded")
    resized = cv2.resize(img, (500,800))
    cv2.imshow("resized image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image Not Loaded")


# cropping image using slicing
cropped_img = resized [00:499,00:300]# [X:X,Y:Y] x = height y = width
cv2.imshow("cropped image", cropped_img)
cv2.imshow("original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# imagerotation
(h,w) = img.shape[:2]
m = cv2.getRotationMatrix2D((w/2,h/2),90,1)
rotated = cv2.warpAffine(img,m,(w,h))
cv2.imshow("rotated", rotated)
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# flipping a image
flipped_img_horizontal = cv2.flip(img,1)

flipped_img_vertical = cv2.flip(img,0)
cv2.imshow("flipped image", flipped_img_horizontal)
cv2.waitKey(0)
cv2.imshow("flipped image", flipped_img_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()

