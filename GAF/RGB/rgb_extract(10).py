import cv2 as cv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

img = cv.imread('../1GASF_abnormal_201.png')
img2 = cv.imread('../1GASF2_normal_201.png')
b,g,r = cv.split(img)
b2,g2,r2 = cv.split(img2)

plt.plot(b.flatten())
plt.plot(b2.flatten())
plt.ylabel('Range Warna')
plt.xlabel('Panjang Data')
# plt.ylim(0,None)
# plt.xlim(0,200)
plt.show()


