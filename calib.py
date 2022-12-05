# Import more libraries
import numpy as np
import glob
import matplotlib.pyplot as plt
import cv2
boardHeight = 13
boardWidth = 7
# Prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((boardHeight*boardWidth,3), np.float32)
objp[:,:2] = np.mgrid[0:boardWidth, 0:boardHeight].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane.
# Make a list of calibration images
images = glob.glob('image/bg.jpg')
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
    else:
        print("Error")
cv2.destroyAllWindows()