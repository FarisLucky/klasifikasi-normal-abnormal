# Author: Johann Faouzi <johann.faouzi@gmail.com>
# License: BSD-3-Clause

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.axes_grid1 import ImageGrid
from pyts.image import GramianAngularField
import numpy as np
import xlrd

file_location = "Book1.xlsx"
wb = xlrd.openworkbook(file_location)
sheet = wb.sheet_by_index(0)

print(sheet.cell_value)

# # Transform the time series into Gramian Angular Fields
# gasf = GramianAngularField(image_size=30, method='summation')
# X_gasf = gasf.fit_transform(X)
# X_gasf2 = gasf.fit_transform(X2)
# # gadf = GramianAngularField(image_size=30, method='difference')
# # X_gadf = gadf.fit_transform(X)

# # Show the images for the first time series
# fig = plt.figure(figsize=(8, 4))
# grid = ImageGrid(fig, 111,
#                  nrows_ncols=(1, 2),
#                  axes_pad=0.15,
#                  share_all=True,
#                  cbar_location="right",
#                  cbar_mode="single",
#                  cbar_size="7%",
#                  cbar_pad=0.3,
#                  )
# images = [X_gasf[0], X_gasf2[0]]
# titles = ['GASF_abnormal_30', 'GASF2_normal_30']
# for image, title, ax in zip(images, titles, grid):
#     im = ax.imshow(image, origin='lower')
#     ax.set_title(title, fontdict={'fontsize': 12})
# ax.cax.colorbar(im)
# ax.cax.toggle_label(True)
# plt.suptitle('Gramian Angular Fields', y=0.98, fontsize=16)
# plt.show()