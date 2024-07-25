import cv2
img = cv2.imread("asset/image2.png")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()