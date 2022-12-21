import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt

model = torch.hub.load('ultralytics/yolov5', 'custom', path='cobest.pt', force_reload=True)
img = cv2.imread('1.jpg')
model.eval()
results = model(img)
bboxes = results.xyxy
print("box",bboxes[1])

# %matplotlib inline 
plt.imshow(np.squeeze(results.render()))
plt.show()