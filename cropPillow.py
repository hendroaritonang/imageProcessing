import cv2
from PIL import Image
image = Image.open("asset/hendro.png")
image.show()
cropped = (50,400,50,600)
img_crop = image.crop(cropped)
img_crop.show()