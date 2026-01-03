import cv2

# Ask user for image path
path = input("Enter image path: ")

img = cv2.imread(path)

if img is None:
    print("❌ Image not found")
else:
    cv2.imshow("User Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

nameof = input("Enter file name: ")
cv2.imwrite(f"{nameof}.png", img)
