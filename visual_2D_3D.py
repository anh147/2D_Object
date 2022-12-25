# importing two required module
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches

A = [1, 2, 3, 4 ,5,6,7,8,9,10]

#image 6
measure6 = np.array([[6.7, 7.5], [9.45,9.35], [14.4,10], [6.8, 4.45], [18.6, 8.1], [8.55,3.65], [20.7,11.1], [24.3,6.2], [16, 4.9], [20.05, 3.9]])
predict6 = np.array([[6.73, 7.45],[9.54, 9.3],[14.46, 9.9],[6.84, 4.35],[18.62, 8.02],[8.61, 3.72],[20.8, 11.1],[24.41, 6.07],[16.09, 4.8],[20.07,3.8]])
loss_2D = abs(measure6-predict6)
#image3D
measure3D = np.array([[29.8, 7.2], [27.1, 14], [23.2, 4.1], [24.8, 14.4], [23.8, 8.9], [22.2, 9.1], [17.5, 9], [30.55, 3.9], [22.55, 10.9], [24, 5.1]])
predict3D = np.array([[29.77, 7.08], [27.27, 13.42] , [23.48, 4.1], [25.06, 14.02], [24.15, 8.73], [22.42, 9.08], [17.55, 8.97], [30.45, 4.07], [22.45, 10.7], [23.58,5.02]])
predict3D_yolo = np.array([[30.32, 6.73],[27.69, 13.22],[23.53,3.47],[25.22, 14.6],[24.23, 8.55],[22.54, 8.92],[17.55, 8.85],[31.2, 3.45],[23.3,10.21 ],[24.3, 4.85]])
loss_3D = abs(measure3D-predict3D)
loss_3D_yolo = abs(measure3D-predict3D_yolo)

print('sum los', sum(loss_3D[:,0])/10)
# plt.scatter(A, loss_2D[:,0], color = 'green')
# plt.scatter(A, loss_3D[:,0], color='red')
# plt.scatter(A, loss_3D_yolo[:,0], color='black')

# Creating figure and axis objects using subplots()
# fig, ax = plt.subplots(figsize=[9, 7])
plt.figure()

plt.subplot(211)

plt.plot(A,loss_2D[:,0],marker='o', linewidth=2, label='2D')
plt.plot(A,loss_3D_yolo[:,0],marker='o', linewidth=2, label='3D_yolo')
plt.plot(A,loss_3D[:,0],marker='o', linewidth=2, label='3D_calib')
plt.title('Sai số theo trục x')
plt.legend()

plt.subplot(212)
plt.plot(A,loss_2D[:,1],marker='o', linewidth=2, label='2D')
plt.plot(A,loss_3D_yolo[:,1],marker='o', linewidth=2, label='3D_yolo')
plt.plot(A,loss_3D[:,1],marker='o', linewidth=2, label='3D_calib')

# ax.plot(X3,Y3,marker='o', linewidth=2, label='Fold 2')
# ax.plot(X4,Y4,marker='o', linewidth=2, label='Fold 3')
# ax.plot(X5,Y5,marker='o', linewidth=2, label='Fold 4')

plt.xticks(rotation=0)
# ax.set_xlabel('Mẫu')
# ax.set_ylabel('Sai số')
plt.title('Sai số theo trục y')
plt.legend()
plt.show()