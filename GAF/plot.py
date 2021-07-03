import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("Book3.xlsx",usecols=[0,1,2,3,4,5,6,7],sheet_name='Sheet1')
df1 = np.reshape(df[4].to_numpy(),(1,60))
sheet2 = pd.read_excel("Book3.xlsx",usecols=[0,1,2,3,4,5,6,7],sheet_name='Sheet2')
ab1 = np.reshape(sheet2[4].to_numpy(),(1,60))
sheet3 = pd.read_excel("Book3.xlsx",usecols=[0,1,2,3,4,5,6,7],sheet_name='normal3lapis')
n3lapis = np.reshape(sheet3[4].to_numpy(),(1,60))
x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(df1[0],label='normal')  # Plot some data on the axes.
ax.plot(ab1[0],label='abnormal')  # Plot more data on the axes...
ax.plot(n3lapis[0],label='masker 3 lapis')  # Plot more data on the axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()