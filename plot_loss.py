# importing two required module
import numpy as np
import matplotlib.pyplot as plt
import math
A = [1, 2, 3, 4 ,5,6,7,8]
#image 5
measure = np.array([[30.4, 7.4], [29.8, 7.1], [19.6,10.5], [29.4,5.8], [27.6,8.5], [27,11.8], [26.3,10.4], [23.1,5.7]])
predict = np.array([[30.472, 6.97], [29.87, 6.86], [19.63,9.93], [29.59,5.33], [27.72,8.16], [27.17, 11.54], [26.29, 10.14], [22.91, 5.15]])

#image 6
measure6 = np.array([[6.7, 7.5], [9.45,9.35], [14.4,10], [6.8, 4.45], [18.6, 8.1], [8.55,3.65], [20.7,11.1], [24.3,6.2], [16, 4.9], [20.05, 3.9]])
predict = np.array([[6.73, 7.45],[9.54, 9.3],[14.46, 9.9],[6.84, 4.35],[18.62, 8.02],[8.61, 3.72],[20.8, 11.1],[24.41, 6.07],[16.09, 4.8],[20.07,3.8]])
print(np.shape(measure))

plt.scatter(measure[:,0], measure[:,1])


# Plotting point using scatter method
plt.scatter(predict[:,0], predict[:,1], color='red')
plt.show()
    
