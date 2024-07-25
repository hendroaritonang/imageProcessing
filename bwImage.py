import cv2
import os
import datetime

def save_image_with_timestamp(image, filename_prefix, output_dir):
    """Saves an image with a timestamped filename in the specified output directory.

    Args:
        image: The image to be saved.
        filename_prefix: The prefix for the filename.
        output_dir: The output directory path.
    """

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"{filename_prefix}_{timestamp}.png")
    cv2.imwrite(output_path, image)

image_path = r'storage/image'
image_directory = r'storage'
output_dir = r'storage'  


if not os.path.exists(output_dir):
    os.makedirs(output_dir)


image = cv2.imread("asset/hendro.png")

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(th, bw) = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)

save_image_with_timestamp(grayscale, "grayscale", output_dir)
save_image_with_timestamp(bw, "bw", output_dir)

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale", grayscale)
cv2.imshow("BW Image", bw)
cv2.waitKey(0)
cv2.destroyAllWindows()