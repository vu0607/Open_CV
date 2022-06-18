import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('105180399.jpg')

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape[:2], 'uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)
# masked = cv.bitwise_and(gray_img, gray_img, mask=mask)

#Grayscale Histogram
""" gray_hist = cv.calcHist([gray_img], [0], mask, [256], [0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show() """

#Color Histogram
masked = cv.bitwise_and(img, img, mask=mask)
# img_hist = cv.calcHist([img], [0], mask, [256], [0,256])
colors =  ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img],[i], mask, [256], [0,256]) 
    plt.plot(hist, color= col)
    plt.xlim([0,256])
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.show()   
cv.imshow('Masked', masked)
cv.waitKey()