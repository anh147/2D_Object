import cv2

img = cv2.imread('image/01.jpg')
bg = cv2.imread('image/bg.jpg')



image = cv2.circle(img, (95, 555), radius=0, color=(0, 0, 255), thickness=10)
cv2.imshow("draw", image)
cv2.waitKey(0)