from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
img = Image.open('asset/image2.png')
plt.imshow(img, cmap=cm.gray)
plt.show()