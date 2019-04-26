import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

from skimage.feature import hog
from skimage import data, exposure

image = cv2.imread("images/orbh4.png")

# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fd, hog_image = hog(image, orientations=8, pixels_per_cell=(3, 3), cells_per_block=(1, 1), block_norm='L2-Hys', visualize=True, multichannel=True)

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

print(hog_image_rescaled.shape)

imgplot = plt.imshow(hog_image_rescaled)#, cmap=plt.cm.gray)
imgplot.axes.get_xaxis().set_visible(False)
imgplot.axes.get_yaxis().set_visible(False)
plt.show()