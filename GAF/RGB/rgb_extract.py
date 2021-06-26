import cv2 as cv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
img = cv.imread('../Summation.png')
img2 = cv.imread('../Summation21.png')
b,g,r = cv.split(img)
b2,g2,r2 = cv.split(img2)
# print(b)
# print(g)
# print(r)
zeros = np.zeros(img.shape[:2], dtype="uint8")
cur_img = img.copy()
cur_img[:, :, 0] = 0
cur_img[:, :, 1] = 0

Red = cv.merge([zeros,zeros,r])
Green = cv.merge([zeros,g,zeros])
Blue = cv.merge([b,zeros,zeros])
plt.plot(r.flatten())
plt.plot(r2.flatten())
plt.ylabel('some numbers')
plt.show()
# cv.imshow("Red Channel", cv.merge([zeros,zeros,r]))
# cv.imshow("Green Channel", cv.merge([zeros,g,zeros]))
# cv.imshow("Blue Channel", cv.merge([b,zeros,zeros]))
# cv.waitKey(0)
# cv.destroyAllWindows()


