import cv2

img = cv2.imread('image/01.jpg')
bg = cv2.imread('image/bg.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,27,4)

# bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
# bg = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,27,4)
cv2.imshow("01", img)
cv2.waitKey(0)

# cv2.imshow("bg", bg)
# cv2.waitKey(0)

# cv2.imshow("sub", bg - img)
# cv2.waitKey(0)

threshold_value = 10
max_val = 255
ret, image = cv2.threshold(img, threshold_value, max_val, cv2.THRESH_BINARY)
cv2.imshow('BinaryThresholding', image)
cv2.waitKey(0)