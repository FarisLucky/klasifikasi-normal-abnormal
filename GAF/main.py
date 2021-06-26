# Author: Johann Faouzi <johann.faouzi@gmail.com>
# License: BSD-3-Clause

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.axes_grid1 import ImageGrid
from pyts.image import GramianAngularField
from pyts.datasets import load_gunpoint
from PIL import Image
import numpy as np
# Parameters
X = [[
    32.7,
    32.6,
    32.6,
    32.7,
    32,
    32.1,
    31.9,
    32.1,
    32.6,
    32.6,
    32,
    32,
    32,
    32.6,
    32.6,
    32.5,
    32.3,
    32.3,
    32.1,
    32.1,
    32.5,
    32.6,
    32.5,
    32.2,
    32.2,
    32.5,
    32.8,
    32.9,
    32.8,
    32.6,
    32.4
]]
X2 = [[
    34.9,
    35,
    35.9,
    34.3,
    34.3,
    34.4,
    33.8,
    34.4,
    33.7,
    34.4,
    34.9,
    34,
    34.8,
    33.5,
    34.2,
    34,
    33.4,
    34.7,
    33.4,
    34.6,
    34.7,
    33.3,
    33.2,
    34.1,
    33.8,
    33.7,
    34.1,
    34.5,
    34.3,
    34,
    34.6,
]]

# Transform the time series into Gramian Angular Fields
gasf = GramianAngularField(image_size=30, method='summation')
X_gasf = gasf.fit_transform(X)
X_gasf2 = gasf.fit_transform(X2)
# gadf = GramianAngularField(image_size=30, method='difference')
# X_gadf = gadf.fit_transform(X)

# Show the images for the first time series
fig = plt.figure(figsize=(8, 4))
grid = ImageGrid(fig, 111,
                 nrows_ncols=(1, 2),
                 axes_pad=0.15,
                 share_all=True,
                 cbar_location="right",
                 cbar_mode="single",
                 cbar_size="7%",
                 cbar_pad=0.3,
                 )
images = [X_gasf[0], X_gasf2[0]]
titles = ['Summation', 'Summation2']
for image, title, ax in zip(images, titles, grid):
    im = ax.imshow(image, origin='lower')
    ax.set_title(title, fontdict={'fontsize': 12})
    mpimg.imsave(title+"1.png",image,format='png')
ax.cax.colorbar(im)
ax.cax.toggle_label(True)
plt.suptitle('Gramian Angular Fields', y=0.98, fontsize=16)
plt.show()