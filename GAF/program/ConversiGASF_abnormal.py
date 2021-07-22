import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.axes_grid1 import ImageGrid
from pyts.image import GramianAngularField
import numpy as np
import pandas as pd
import numpy as np

df = pd.read_excel("../dataset/dataset_mentah.xlsx",usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],sheet_name='abnormal_2')
# np.reshape(df["nama_kolom"].to_numpy(), (1,60))
df1 = np.reshape(df['i'].to_numpy(),(1,60))
df2 = np.reshape(df['j'].to_numpy(),(1,60))
df3 = np.reshape(df['k'].to_numpy(),(1,60))
df4 = np.reshape(df['l'].to_numpy(),(1,60))
df5 = np.reshape(df['m'].to_numpy(),(1,60))
df6 = np.reshape(df['n'].to_numpy(),(1,60))
df7 = np.reshape(df['o'].to_numpy(),(1,60))
df8 = np.reshape(df['p'].to_numpy(),(1,60))

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
titles = ['AB_1', 'AB_2','AB_3','AB_4','AB_5','AB_6','AB_7','AB_8']
# i = 0
rows = 2
columns = 6
for image, title, ax in zip(images, titles, grid):
    im = ax.imshow(image, origin='lower')
    ax.set_title(title, fontdict={'fontsize': 12})
    # mpimg.imsave("n/"+title+str(i)+".png",image,format='png')
    mpimg.imsave("../testing/ab_2/"+title+"_2.png",image,format='png')
    # mpimg.imsave("ab/"+title+str(i)+"1.png",images2[i],format='png')
    # i+=1
# ax.cax.colorbar(im)
# ax.cax.toggle_label(True)
# plt.suptitle('Gramian Angular Fields', y=0.98, fontsize=16)
# plt.show()