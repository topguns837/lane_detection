import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# Create a custom kernel
# 3x3 array for edge detection
sobel_y = np.array([[ -1, -2, -1],
 [ 0, 0, 0],
 [ 1, 2, 1]])
## TODO: Create and apply a Sobel x operator
sobel_x = np.array([[-1,0,1],
 [ -2, 0 , 2],
 [ -1,0,1]])

img1=cv.imread('img/sample_2.jpeg')

# Filter the image using filter2D, which has inputs: (grayscale image, bitdepth, kernel)
filtered_image_y = cv.filter2D(img1, -1, sobel_y)
filtered_image_x = cv.filter2D(img1, -1, sobel_x)
plt.subplot(2,2,1),plt.imshow(img1,cmap = 'gray')
plt.title('Gray scale'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(filtered_image_x,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(filtered_image_y,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()