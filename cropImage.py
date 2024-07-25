import cv2
image = cv2.imread("asset/hendro.png")
cv2.imshow("Original Image", image)
cropped = image[50:400,50:600]
cv2.imshow("Crop Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()