import cv2

img = cv2.imread('image/03.jpg', cv2.IMREAD_GRAYSCALE)
img_bg = cv2.imread('image/bg.jpg', cv2.IMREAD_GRAYSCALE)

thresh = 150
im_bw = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
im_bw_bg = cv2.threshold(img_bg, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("draw", im_bw_bg )
cv2.waitKey(0)

cv2.imshow("draw", im_bw )
cv2.waitKey(0)


image = cv2.circle(img, (95, 555), radius=0, color=(0, 0, 255), thickness=10)
cv2.imshow("draw",im_bw -  im_bw_bg )
cv2.waitKey(0)