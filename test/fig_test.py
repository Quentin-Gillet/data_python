import numpy as np
import matplotlib.pyplot as plt

# plt.figure creates a matplotlib.figure.Figure instance
fig = plt.figure()
rect = fig.patch # a rectangle instance

ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.5])
rect = ax1.patch

plt.bar([0,1,2,3,4], [4,5,6,7,6])

for label in ax1.xaxis.get_ticklabels():
    # label is a Text instance
    label.set_rotation(45)
    label.set_fontsize(10)

plt.show()
