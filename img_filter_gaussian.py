#importing required packages
import numpy as np
import cv2
import math
import matplotlib.image as img
import matplotlib.pyplot as mtpl
# Image on which the filter is applied
gauss_image = cv2.imread('IMG2.JPG')
# converting colors to hsv

gauss_image = cv2.cvtColor(gauss_image, cv2.COLOR_BGR2HSV) # convert to HSV
# X and Y dimesions of image
figsize = 15
gaussblur_image = cv2.GaussianBlur(gauss_image, (figsize, figsize),5) # it take 3 parameters
mtpl.figure(figsize=(20,15))
mtpl.subplot(121), mtpl.imshow(cv2.cvtColor(gauss_image, cv2.COLOR_HSV2RGB)),mtpl.title('Image before applying Gaussian filter')
mtpl.xticks([]), mtpl.yticks([])
mtpl.subplot(122), mtpl.imshow(cv2.cvtColor(gaussblur_image, cv2.COLOR_HSV2RGB)),mtpl.title('Image after applying Gaussian Filter')
mtpl.xticks([]), mtpl.yticks([])
mtpl.show()