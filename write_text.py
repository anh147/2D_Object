# Python program to explain cv2.putText() method
    
# importing cv2
import cv2
    
# path
path = 'image/n_bg.jpg'
    
# Reading an image in default mode
image = cv2.imread(path)
    
# Window name in which image is displayed
window_name = 'Image'
  
# text
text = '(0,0)'
  
# font
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (1200, 90)
  
# fontScale
fontScale = 1
   
# Red color in BGR
color = (0, 0, 255)
  
# Line thickness of 2 px
thickness = 2
   
# Using cv2.putText() method
image = cv2.putText(image, text, org, font, fontScale, 
                 color, thickness, cv2.LINE_AA, False)
  
image = cv2.circle(image, (1188, 103), radius=0, color=(0, 200, 255), thickness=10)
  
# Displaying the image
cv2.imshow(window_name, image) 
cv2.waitKey(0)