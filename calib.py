# Import more libraries
import numpy as np
import glob
import matplotlib.pyplot as plt
import cv2
boardHeight = 12
boardWidth = 7
# Prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((boardHeight*boardWidth,3), np.float32)
objp[:,:2] = np.mgrid[0:boardWidth, 0:boardHeight].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane.
# Make a list of calibration images
images = glob.glob('image3/bg.jpg')
# Step through the list and search for chessboard corners
for idx, fname in enumerate(images):
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (boardWidth,boardHeight), None)
# If found, add object points, image points
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)
# Draw and display the corners
        cv2.drawChessboardCorners(img, (boardWidth,boardHeight), corners, ret)
        #write_name = 'corners_found'+str(idx)+'.jpg'
        #cv2.imwrite(write_name, img)
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.imwrite('image/n_bg_corners.jpg', img)
    else:
        print("Error")
cv2.destroyAllWindows()

print("objpoints", objpoints)
print("imgpoints", imgpoints)

print(np.shape(imgpoints))
point = np.array(imgpoints)
point = point.flatten()
print(np.shape(imgpoints))
print(imgpoints[0][1][0])


img = cv2.imread('image3/00.jpg')
for i in range (0, boardHeight*boardWidth):
    image = cv2.circle(img, (int(imgpoints[0][i][0][0]), int(imgpoints[0][i][0][1])), radius=0, color=(0, 0, 255), thickness=10)

cv2.imshow('draw', image)
cv2.waitKey(0)