import matplotlib.pyplot as plt
import numpy as np
x_axis = np.array([100, 40, 80, 1])
y_axis = np.array([500, 15, 25, 44])
plt.plot(x_axis, y_axis, marker = 'o', linestyle ='dashdot', color ="red")#fmt standard
plt.show()