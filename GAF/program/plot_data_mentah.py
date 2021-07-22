import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("../dataset/dataset_mentah.xlsx",usecols=[0,1,2,3,4,5],sheet_name='normal_60')
df1 = np.reshape(df["salman_new (d-2)"].to_numpy(),(1,60))
# df2 = np.reshape(df["ibnu M-1(d-2)"].to_numpy(),(1,200))
df3 = np.reshape(df["ibnu M-1(d-2)"].to_numpy(),(1,60))
df4 = np.reshape(df["dani M-3(d-3)"].to_numpy(),(1,60))
df5 = np.reshape(df["ani M-kn95"].to_numpy(),(1,60))
# print(df1)
# quit()
# # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(df1[0],label='tanpa masker',linewidth=1.5)
# ax.plot(df2[0],label='masker 1 lapis')
ax.plot(df3[0],label='masker 1 lapis',linewidth=1.4)
ax.plot(df4[0],label='masker 3 lapis',linewidth=1.3)
ax.plot(df5[0],label='masker KN95',linewidth=1.3)
ax.set_xlabel('jumlah frame')
ax.set_ylim([29,35]) # set range y axes
ax.set_ylabel('suhu celcius')
ax.set_title("Plot Data Mentah")
ax.legend()  # Add a legend.
plt.show()