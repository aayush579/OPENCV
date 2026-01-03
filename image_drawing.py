import cv2

img = cv2.imread("parrot.jpg")

# if img is not None:
#     print ("image loaded")
# else:print("image not loaded")
# pt1 = (50,100) #starting point
# pt2 = (100,100) #ending point
# color = (255,0,0)
# thickness = 2
#
# cv2.line(img,pt1,pt2,color,thickness)
# cv2.imshow("line",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # drawing a rectangle
# pt3 = (50,100) #starting point
# pt4 = (150,200) #ending point
# color = (255,0,0)
# thickness = 2
#
# cv2.rectangle(img,pt3,pt4,color,thickness)
# cv2.imshow("rectangle",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#

center = (img.shape[1] / 2, img.shape[0] / 2)
cv2.circle(img, (50,100), 60, (255, 0, 0 ), 2)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()