#import relevant libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc,ndimage

#import image file
brain_image=plt.imread('/Users/ishitaarun/Desktop/Brain.jpg')

#find the dimensions of the original image
dimensions=brain_image.shape
print(dimensions)

#draw the original image
plt.imshow(brain_image, cmap='Greys_r')

#save the original image file
plt.savefig('original.png', dpi=300, bbox_inches='tight')

#close the image file (if this was not closed, the histogram was created on the image file)
plt.close()

#plot histogram of the image
hist_original = plt.hist(brain_image, bins=10)
#save the histogram for the original image
plt.savefig('original_hist.png', dpi=300, bbox_inches='tight')
#save the histogram of the original image
plt.close()

#sigma=5
brain_image_5=ndimage.gaussian_filter(brain_image, sigma=5) #smooth the image with sigma=5 
plt.imshow(brain_image_5, cmap='Greys_r') #draw the image in greyscale
plt.savefig('smoothened_5.png', dpi=300, bbox_inches='tight') #save the image
plt.close() #close the image file
hist_5=plt.hist(brain_image_5, bins=10) #plot histogram for the smoothened image
plt.savefig('original_hist_5.png', dpi=300, bbox_inches='tight') #save the histogram for the smoothened image
plt.close() #close the histogram file

#sigma=10
brain_image_10=ndimage.gaussian_filter(brain_image, sigma=10) #smooth the image with sigma=10
plt.imshow(brain_image_10, cmap='Greys_r') #draw the image in greyscale
plt.savefig('smoothened_10.png', dpi=300, bbox_inches='tight') #save the image
plt.close() #close the image file
hist_10=plt.hist(brain_image_10, bins=10) #plot histogram for the smoothened image
plt.savefig('original_hist_10.png', dpi=300, bbox_inches='tight') #save the histogram for the smoothened image
plt.close() #close the histogram file

#sigma=20
brain_image_20=ndimage.gaussian_filter(brain_image, sigma=20) #smooth the image with sigma=20
plt.imshow(brain_image_20, cmap='Greys_r') #draw the image in greyscale
plt.savefig('smoothened_20.png', dpi=300, bbox_inches='tight') #save the image
plt.close() #close the image file
hist_20=plt.hist(brain_image_20, bins=10) #plot histogram for the smoothened image
plt.savefig('original_hist_20.png', dpi=300, bbox_inches='tight') #save the histogram for the smoothened image
plt.close() #close the histogram file

#sigma=30
brain_image_30=ndimage.gaussian_filter(brain_image, sigma=30) #smooth the image with sigma=30
plt.imshow(brain_image_30, cmap='Greys_r') #draw the image in greyscale
plt.savefig('smoothened_30.png', dpi=300, bbox_inches='tight') #save the image
plt.close() #close the image file
hist_30=plt.hist(brain_image_30, bins=10) #plot histogram for the smoothened image
plt.savefig('original_hist_20.png', dpi=300, bbox_inches='tight') #save the histogram for the smoothened image
plt.close() #close the histogram file

#sigma=40
brain_image_40=ndimage.gaussian_filter(brain_image, sigma=40) #smooth the image with sigma=40
plt.imshow(brain_image_40, cmap='Greys_r') #draw the image in greyscale
plt.savefig('smoothened_40.png', dpi=300, bbox_inches='tight') #save the image
plt.close() #close the image file
hist_40=plt.hist(brain_image_40, bins=10) #plot histogram for the smoothened image
plt.savefig('original_hist_40.png', dpi=300, bbox_inches='tight') #save the histogram for the smoothened image
plt.close() #close the histogram file

#sigma=50
brain_image_50=ndimage.gaussian_filter(brain_image, sigma=50) #smooth the image with sigma=50
plt.imshow(brain_image_50, cmap='Greys_r') #draw the image in greyscale
plt.savefig('smoothened_50.png', dpi=300, bbox_inches='tight') #save the image
plt.close() #close the image file
hist_50=plt.hist(brain_image_50, bins=10) #plot histogram for the smoothened image
plt.savefig('original_hist_50.png', dpi=300, bbox_inches='tight') #save the histogram for the smoothened image
plt.close() #close the histogram file
