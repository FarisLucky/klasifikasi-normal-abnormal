import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.axes_grid1 import ImageGrid
from pyts.image import GramianAngularField
import numpy as np
import pandas as pd

df = pd.read_excel("Book3.xlsx",usecols=[0,1,2,3,4,5,6,7],sheet_name='normal3lapis')
df1 = np.reshape(df[1].to_numpy(),(1,60))
df2 = np.reshape(df[2].to_numpy(),(1,60))
df3 = np.reshape(df[3].to_numpy(),(1,60))
df4 = np.reshape(df[4].to_numpy(),(1,60))
df5 = np.reshape(df[5].to_numpy(),(1,60))
df6 = np.reshape(df[6].to_numpy(),(1,60))
df7 = np.reshape(df[7].to_numpy(),(1,60))
df8 = np.reshape(df[8].to_numpy(),(1,60))

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
titles = ['GASF', 'GASF2','GASF3','GASF4','GASF5','GASF6','GASF7','GASF8']
i = 0
rows = 2
columns = 6
for image, title, ax in zip(images, titles, grid):
    mpimg.imsave("n3lapis/"+title+str(i)+".png",image,format='png')