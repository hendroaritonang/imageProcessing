import cv2
image = cv2.imread("asset/hendro.png")
cv2.imshow("Original Image", image)
x, y, w, h = 120, 10, 400, 450
cropped = image[y:y+h, x:x+w]
cv2.imshow("Crop Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()