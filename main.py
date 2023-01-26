# Importing modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2 as cv


image=cv.imread('img/sample_2.jpeg')
height=image.shape[0]
width=image.shape[1]
img=np.copy(image)


def region_of_interst(img,vertices):
    mask = np.zeros_like(img)

    #channel_count = img.shape[2]

    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)

    masked_image = cv.bitwise_and(img, mask)
    return masked_image

region_of_interest_vertices = [
 (0, height),
 (width / 2, height / 2),
 (width, height),]

gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
canny=cv.Canny(gray,100,200)
cropped_image = region_of_interst(canny,np.array([region_of_interest_vertices],np.int32))


cv.imshow("Output", cropped_image)

if cv.waitKey(0) & 0xFF == ord('q'):
    exit()