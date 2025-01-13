import matplotlib.pyplot as plt
import numpy as np
x_axis =np.array([1, 15, 40, 20 ,5])
y_axis = np.array([10, 180, 15, 50, 40])
plt.plot(y_axis, marker = 'o', linestyle = "dashed", color = "black")
plt.title('REAL TIME ANALYSIS')
plt.xlabel('x Axis')
plt.ylabel('y Axis')
plt.show()

x_axis =np.array([0, 6])
y_axis =np.array([0, 250])
plt.plot(x_axis, y_axis, "o")
plt.show()

x_axis =np.array([1, 2, 6, 8])
y_axis =np.array([3, 8, 1, 10])
plt.plot(x_axis, y_axis)
plt.show()


 
#print(dir(np))  # this line prints all the data of a module



         
                
                