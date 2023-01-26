import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# read the image
img1 = cv.imread('img/sample_2.jpeg',0)
# remove noise
img = cv.GaussianBlur(img1,(3,3),0)
# convolute with proper kernels
laplacian = cv.Laplacian(img,cv.CV_64F)


plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.show()