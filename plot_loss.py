# importing two required module
import numpy as np
import matplotlib.pyplot as plt
import math

measure = np.array([[30.4, 7.4], [29.8, 7.1], [19.6,10.5], [29.4,5.8], [27.6,8.5]])
predict = np.array([[30.472, 6.97], [29.87, 6.86], [19.63,9.93], [29.59,5.33], [27.72,8.16]])
print(np.shape(measure))

plt.scatter(measure[:,0],measure[:,1])


# Plotting point using scatter method
plt.scatter(predict[:,0],predict[:,1], color='red')
plt.show()
    
