#import relevant libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc,ndimage

#import image file
brain_image=plt.imread('/Users/ishitaarun/Desktop/Brain.jpg')

#find the dimensions of the original image
dimensions=brain_image.shape

#draw the original image
plt.imshow(brain_image, cmap='Greys_r')

#display the original image 
plt.show()

#plot histogram of the image
hist_original = plt.hist(brain_image, bins=10, align='mid', orientation='vertical', stacked=False)
plt.show()

#smoothing the image
brain_image_5=ndimage.gaussian_filter(brain_image, sigma=5)
brain_image_10=ndimage.gaussian_filter(brain_image, sigma=10)
brain_image_20=ndimage.gaussian_filter(brain_image, sigma=20)
brain_image_30=ndimage.gaussian_filter(brain_image, sigma=30)
brain_image_40=ndimage.gaussian_filter(brain_image, sigma=40)
brain_image_50=ndimage.gaussian_filter(brain_image, sigma=50)

#draw the smoothened images
plt.imshow(brain_image_5, cmap='Greys_r')
plt.imshow(brain_image_10, cmap='Greys_r')
plt.imshow(brain_image_20, cmap='Greys_r')
plt.imshow(brain_image_30, cmap='Greys_r')
plt.imshow(brain_image_40, cmap='Greys_r')
plt.imshow(brain_image_50, cmap='Greys_r')

#display the smoothened images
plt.show()

#plotting histogram for smoothened images
hist_5=plt.hist(brain_image_5, bins=10, align='mid', orientation='vertical', stacked=False)
hist_10=plt.hist(brain_image_10, bins=10, align='mid', orientation='vertical', stacked=False)
hist_20=plt.hist(brain_image_20, bins=10, align='mid', orientation='vertical', stacked=False)
hist_30=plt.hist(brain_image_30, bins=10, align='mid', orientation='vertical', stacked=False)
hist_40=plt.hist(brain_image_40, bins=10, align='mid', orientation='vertical', stacked=False)
hist_50=plt.hist(brain_image_50, bins=10, align='mid', orientation='vertical', stacked=False)
