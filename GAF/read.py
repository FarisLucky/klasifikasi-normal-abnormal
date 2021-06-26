import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.axes_grid1 import ImageGrid
from pyts.image import GramianAngularField
import numpy as np
import pandas as pd
import numpy as np

df = pd.read_excel("Book1.xlsx",usecols=[0,1,2,3,4,5,6,7],sheet_name='Sheet1')
df1 = np.reshape(df[1].to_numpy(),(1,60))
df2 = np.reshape(df[2].to_numpy(),(1,60))
df3 = np.reshape(df[3].to_numpy(),(1,60))
df4 = np.reshape(df[4].to_numpy(),(1,60))
df5 = np.reshape(df[5].to_numpy(),(1,60))
df6 = np.reshape(df[6].to_numpy(),(1,60))
df7 = np.reshape(df[7].to_numpy(),(1,60))
df8 = np.reshape(df[8].to_numpy(),(1,60))

sheet2 = pd.read_excel("Book1.xlsx",usecols=[0,1,2,3,4,5,6,7],sheet_name='Sheet2')
ab1 = np.reshape(sheet2[1].to_numpy(),(1,60))
ab2 = np.reshape(sheet2[2].to_numpy(),(1,60))
ab3 = np.reshape(sheet2[3].to_numpy(),(1,60))
ab4 = np.reshape(sheet2[4].to_numpy(),(1,60))
ab5 = np.reshape(sheet2[5].to_numpy(),(1,60))
ab6 = np.reshape(sheet2[6].to_numpy(),(1,60))
ab7 = np.reshape(sheet2[7].to_numpy(),(1,60))
ab8 = np.reshape(sheet2[8].to_numpy(),(1,60))

# Transform the time series into Gramian Angular Fields
gasf = GramianAngularField(image_size=60, method='summation')
X_gasf1 = gasf.fit_transform(df1)
X_gasf2 = gasf.fit_transform(df2)
X_gasf3 = gasf.fit_transform(df3)
X_gasf4 = gasf.fit_transform(df4)
X_gasf5 = gasf.fit_transform(df5)
X_gasf6 = gasf.fit_transform(df6)
X_gasf7 = gasf.fit_transform(df7)
X_gasf8 = gasf.fit_transform(df8)

X_ab_gasf1 = gasf.fit_transform(ab1)
X_ab_gasf2 = gasf.fit_transform(ab2)
X_ab_gasf3 = gasf.fit_transform(ab3)
X_ab_gasf4 = gasf.fit_transform(ab4)
X_ab_gasf5 = gasf.fit_transform(ab5)
X_ab_gasf6 = gasf.fit_transform(ab6)
X_ab_gasf7 = gasf.fit_transform(ab7)
X_ab_gasf8 = gasf.fit_transform(ab8)

# Show the images for the first time series
fig = plt.figure(figsize=(8, 4))
grid = ImageGrid(fig, 111,
                 nrows_ncols=(2, 6),
                 axes_pad=0.15,
                 share_all=True,
                 cbar_location="right",
                 cbar_mode="single",
                 cbar_size="7%",
                 cbar_pad=0.3,
                 )
images = [X_gasf1[0], X_gasf2[0], X_gasf3[0], X_gasf4[0],X_gasf5[0],X_gasf6[0],X_gasf7[0],X_gasf8[0]]
images2 = [X_ab_gasf1[0], X_ab_gasf2[0], X_ab_gasf3[0], X_ab_gasf4[0],X_ab_gasf5[0],X_ab_gasf6[0],X_ab_gasf7[0],X_ab_gasf8[0]]
titles = ['GASF', 'GASF2','GASF3','GASF4','GASF5','GASF6','GASF7','GASF8']
i = 0
rows = 2
columns = 6
for image, title, ax in zip(images, titles, grid):
    # im = ax.imshow(image, origin='lower')
    # ax.set_title(title, fontdict={'fontsize': 12})
    mpimg.imsave("n/"+title+str(i)+".png",image,format='png')
    mpimg.imsave("ab/"+title+str(i)+"1.png",images2[i],format='png')
    i+=1
# ax.cax.colorbar(im)
# ax.cax.toggle_label(True)
# plt.suptitle('Gramian Angular Fields', y=0.98, fontsize=16)
# plt.show()