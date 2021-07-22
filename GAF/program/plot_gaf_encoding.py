import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("../dataset/dataset_mentah.xlsx",usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13],sheet_name='AB BARU TAMBAH')
df1 = np.reshape(df['d'].to_numpy(),(1,60))
# print(df1)
# quit()
# # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(df1[0],label='abnormal',linewidth=1.5)
ax.set_xlabel('jumlah frame')
ax.set_ylim([32,37]) # set range y axes
# ax.set_ylim([26,32]) # set range y axes 3 mask
ax.set_ylabel('suhu celcius')
ax.set_title("Plot Data GAF")
ax.legend()  # Add a legend.
plt.show()